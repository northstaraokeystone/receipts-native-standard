# Contribution Guide

Welcome to the Receipts-Native Standard. This guide explains how to contribute to the standard, tooling, and ecosystem.

---

## Ways to Contribute

### 1. Improve the Standard

**What:** Propose clarifications, new principles, or refinements to the definition.

**How:**
1. Open a GitHub issue describing your proposal
2. Use the "Standard Proposal" template
3. Include:
   - Current problem or gap
   - Proposed change
   - Rationale
   - Impact on existing implementations
4. Participate in 14-day discussion period
5. Steering committee votes on acceptance

**Examples:**
- Clarify edge cases in existing principles
- Propose new compliance tests
- Suggest better terminology

---

### 2. Build Tooling

**What:** Create tools that help others implement receipts-native systems.

**Ideas:**
- Language-specific SDKs (Go, Rust, Java, etc.)
- Compliance test runners
- Receipt visualization tools
- Migration utilities (logging → receipts-native)
- IDE plugins for receipt validation

**How:**
1. Check existing tooling in ecosystem
2. Open issue to discuss before building
3. Build in your own repo
4. Submit PR to add to ecosystem list

---

### 3. Write Documentation

**What:** Improve guides, examples, and explanations.

**Needs:**
- Getting started tutorials
- Domain-specific guides (healthcare, government, autonomous)
- Architecture decision records
- Case studies from implementations

**How:**
1. Open issue or PR with improvement
2. Follow existing documentation style
3. Include practical examples

---

### 4. Implement the Standard

**What:** Build a receipts-native system and share learnings.

**How:**
1. Use the [starter kit](../starter/)
2. Run compliance tests
3. Document your implementation
4. Add to implementations list via PR
5. Consider joining working group

---

### 5. Join the Working Group

**What:** Become a steering committee member and shape the standard.

**Eligibility:**
- Production implementation, OR
- Significant contribution to standard/tooling, OR
- Deep domain expertise

**How:**
1. Open GitHub issue using "Join Working Group" template
2. See [CHARTER.md](./CHARTER.md) for full process

---

## Contribution Standards

### Code

- Include tests for any tooling
- Document public APIs
- Follow language-specific conventions
- MIT or Apache 2.0 license for code

### Documentation

- Clear, concise language
- Practical examples
- Accessible to newcomers and experts

### Issues and PRs

- One topic per issue/PR
- Clear title and description
- Reference related issues
- Respond to feedback within 7 days

---

## Review Process

### Standard Changes

1. **Proposal:** Open issue with rationale
2. **Discussion:** 14-day minimum comment period
3. **Revision:** Author incorporates feedback
4. **Vote:** Steering committee decides (2/3 majority for standard changes)
5. **Implementation:** Update compliance tests
6. **Release:** Publish new version

### Documentation / Tooling

1. **PR:** Submit pull request
2. **Review:** Maintainer reviews within 7 days
3. **Revision:** Address feedback
4. **Merge:** Maintainer merges

---

## Recognition

Contributors are recognized in:
- [MEMBERS.md](./MEMBERS.md) contributors section
- Release notes for significant contributions
- Working group meeting acknowledgments

---

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. All contributors are expected to:

- Be respectful and constructive
- Focus on technical merit
- Welcome newcomers
- Assume good intent

Violations may result in removal from the project.

---

## Questions?

- Open a GitHub issue with the `question` label
- Attend a working group meeting (monthly, starting Feb 2025)

---

*Thank you for contributing to the receipts-native ecosystem!*
