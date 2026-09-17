import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const fixtureUrl = new URL("../fixtures/workspace-shell.html", import.meta.url);
const tokenContractUrl = new URL("../contracts/design-token-categories.json", import.meta.url);
const stateContractUrl = new URL("../contracts/presentation-state.schema.json", import.meta.url);

test("mock shell exposes provenance and non-authoritative status", async () => {
  const html = await readFile(fixtureUrl, "utf8");
  assert.match(html, /data-source-kind="MOCK"/);
  assert.match(html, /data-authoritative="false"/);
  assert.match(html, /NOT LIVE, NOT EVIDENCE, NOT HUMAN APPROVAL/);
});

test("shell keeps availability, authorization, approval, and Evidence distinct", async () => {
  const html = await readFile(fixtureUrl, "utf8");
  for (const label of ["Control availability", "Authorization", "Human approval", "Evidence"]) {
    assert.match(html, new RegExp(`<dt>${label}</dt>`));
  }
  assert.match(html, /disabled aria-disabled="true"/);
  assert.match(html, /disabled control is not authorization enforcement/);
});

test("shell provides structural accessibility cues without claiming conformance", async () => {
  const html = await readFile(fixtureUrl, "utf8");
  for (const landmark of ["<header>", "<main", "<footer>"]) assert.match(html, new RegExp(landmark));
  assert.match(html, /<aside aria-label="[^"]+"/);
  assert.match(html, /aria-describedby="control-note"/);
  assert.match(html, /ⓘ/);
  assert.doesNotMatch(html, /WCAG\s*[0-9]|accessibility conformance/i);
});

test("token contract contains only the NCIE-012 taxonomy and unresolved HR boundary", async () => {
  const contract = JSON.parse(await readFile(tokenContractUrl, "utf8"));
  assert.deepEqual(contract.required, [
    "typographyRoles",
    "spacing",
    "sizing",
    "iconographyRoles",
    "colourRoles",
    "motion",
    "borders",
    "density",
    "stateRoles"
  ]);
  assert.equal(contract.$defs.unresolvedCategory.properties.status.const, "UNRESOLVED");
  assert.equal(contract.$defs.unresolvedCategory.properties.humanReview.const, "HR12-7-1");
});

test("mock presentation-state contract cannot assert governed authority", async () => {
  const contract = JSON.parse(await readFile(stateContractUrl, "utf8"));
  const mockRule = contract.allOf[0].then.properties;
  assert.equal(mockRule.authoritative.const, false);
  assert.equal(mockRule.authorizationState.const, "UNKNOWN");
  assert.deepEqual(mockRule.humanApprovalState.enum, ["NOT_APPLICABLE", "PENDING"]);
  assert.equal(mockRule.evidenceState.const, "NOT_EVIDENCE");
});
