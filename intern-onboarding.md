---
layout: page
title: Internship Program — Applicant & Onboarding Guide
subtitle: How we work, document contributions, and prepare invoices
permalink: /intern-onboarding/
sitemap: false
search: false
head-extra:
  - noindex.html
---

Welcome to Pragament's Full Stack Software Development Engineer (SDE) internship. Read this guide to understand the work expectations, AI-assisted development process, invoicing rules, and travel documentation before you begin.

## 1. Tools and your public work profile

- You will have free access to ChatGPT Codex Pro through office devices.
- Get your profile added to [Our People](https://pragament.com/people/), showcasing the work you have completed so far. Submit a pull request to the [Pragament website repository](https://github.com/Pragament/pragament.github.io) to add or update your profile.
- Update your profile with your latest work at least once a month.

## 2. Start every feature with a GitHub issue

**Create a GitHub issue describing the feature user story before starting work on it.** Include the requirements and acceptance criteria so that completion can be verified against the original scope.

Use AI to divide work into smaller user stories sized XXS, XS, or S. Each billable story must still deliver an independently valuable product feature: a distinct user-facing capability or substantial new system behavior. Splitting implementation steps into separate tasks does not make each step a billable feature.

For each story:

1. Record the user story and acceptance criteria in a GitHub issue.
2. Use Codex or Claude to help implement it.
3. Test the complete feature against every acceptance criterion and resolve any issues.
4. Record the actual effort size and detailed user story in your Excel invoice sheet.
5. Indicate whether the customer is currently using the feature.

## 3. AI-assisted user story sizing

Size a story by the **actual developer effort required to deliver and verify the complete feature**, rather than by lines of code.

| Size | Typical workflow | What it means |
| --- | --- | --- |
| **XXS** | Prompt → Test → Works | Give AI the complete new user story and acceptance criteria. It implements the feature, and developer testing confirms it works with trivial or no corrections. |
| **XS** | Prompt → Test → Minor fixes → Works | AI implements most or all of the story. Testing reveals a few small issues resolved through additional prompts or minor corrections, without significant debugging or redesign. |
| **S** | Prompt → Iterate → Debug → Test → Works | AI produces a substantial implementation, but delivery requires multiple iterations, debugging, integration changes, or developer decisions until all acceptance criteria pass. |

As a quick rule: **XXS** means AI gets it essentially right the first time; **XS** needs minor corrections or re-prompts; **S** needs meaningful developer iteration or debugging.

Your invoice must contain **more XXS stories than XS stories, and more XS stories than S stories**: `XXS count > XS count > S count`. Plan small, independently valuable stories while recording their actual effort honestly.

## 4. What qualifies for invoice billing

**Only 100% completed, new features that meet the initially communicated requirements may be included.** Use AI to help review your invoice and retain only independently valuable product features.

Eligible entries must deliver a distinct user-facing capability or substantial new system behavior. Include the detailed feature user story in the Excel sheet so the delivered value and original requirements are clear.

Do not bill the following as standalone features:

- Bug fixes, hotfixes, or release patches.
- Pure styling, CSS or layout changes, branding or color changes.
- Responsive adjustments, narrow-screen improvements, or other display tweaks.
- Refactoring, formatting, README setup, or implementation-support work.
- Validation polish, input validation, navigation buttons, or thumbnails.

### Invoice information to include

| Field | What to record |
| --- | --- |
| Detailed feature user story | The independently valuable capability and its initially communicated requirements and acceptance criteria. |
| GitHub issue | A reference to the issue created before implementation. |
| Actual story size | XXS, XS, or S, based on delivery and verification effort. |
| Completion | Confirmation that the feature is fully complete and meets the original requirements. |
| Customer currently using it? | A dedicated column indicating whether the feature is currently used by the customer. |
| Project release | The release associated with the completed work. |
| Bonus entries | The bonus entries required under the release rule below. |

### Release bonus rule

Include **at least one bonus entry in the invoice for every 10 tasks completed as part of a project release**. Bug fixes, hotfixes, and release patches are excluded from this rule.

The following release names illustrate the distinction; a version label alone does not make work eligible for billing.

| Example version | Release description | Category |
| --- | --- | --- |
| 1.0.0 | Initial release | New release work; apply the feature eligibility rules above. |
| 1.0.1 | Bug fix release | Excluded maintenance work. |
| 1.1.0 | Minor feature release | New release work; apply the feature eligibility rules above. |
| 1.2.0 | Enhancement release | Apply the feature eligibility rules above. |
| 2.0.0 | Major release | New release work; apply the feature eligibility rules above. |
| 2.1.0 | Feature update | New release work; apply the feature eligibility rules above. |
| 2.1.1 | Patch release | Excluded maintenance work. |
| 2.2.0 | Performance improvement release | Eligible only where the work meets the new-feature or substantial-new-behavior criteria above. |
| 3.0.0 | Major upgrade | New release work; apply the feature eligibility rules above. |
| 3.0.1 | Hotfix release | Excluded maintenance work. |

## 5. Office visits and travel expenses

**A meaningful Full Stack SDE coding contribution is required between each office visit.**

Your travel invoice must be based on attendance recorded in the **punch-in / punch-out app**. Keep those attendance records up to date for office visits.

For travel-expense calculations, send your internship coordinator the following on WhatsApp **four times a month**, covering the areas you travel from and to:

- Your **current location**, sent from a recognizable area landmark. Send a current-location pin, not a live location.
- A selfie with the recognizable landmark visible in the background.

### Increment milestones

| Item | Milestone |
| --- | --- |
| Task increment | After every 20 features. |
| Travel expense increment | After every 20 features and every 20 office visits. |

Confirm the increment amounts and how the feature and office-visit milestones are applied with your coordinator. This guide does not specify amounts or a calculation formula. Also confirm the bonus-entry amount and calculation before preparing your invoice.

## 6. Internship certificate

The duration stated on your **Full Stack Software Development Engineer (SDE) certificate** will be determined by the work documented in your **approved invoices**. Keep your feature records and invoices complete and accurate.

## Before submitting an invoice

- Check that every billed feature is new, fully complete, independently valuable, and meets its original requirements.
- Include detailed user stories, GitHub issue references, actual sizes, and the customer-usage column in the Excel sheet.
- Check that `XXS count > XS count > S count`.
- Include the required release bonus entries and exclude maintenance or polish work.
- Base travel claims on punch-in / punch-out attendance and provide the requested travel documentation.
- Keep your public work profile updated each month.
