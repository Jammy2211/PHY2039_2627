# Repository instructions

## Chirun course workflow

- This repository is the Chirun source for **PHY2039: Scientific Computation
  with Python**, academic year **2026–27**.
- GitHub repository: `https://github.com/Jammy2211/PHY2039_2627`.
- Chirun reads the root `config.yml`. Its `structure` list controls which
  sections and pages appear on the generated homepage; files are not included
  merely because they exist in the repository.
- Active course material belongs in the top-level `content/`, `static/`,
  `notebooks/`, and related source folders. Every `source` named by
  `config.yml` must exist before changes are pushed.
- `archive/2526/` is the untouched reference snapshot of the 2025–26 course.
  Do not edit it unless the user explicitly asks. Make 2026–27 changes in the
  active top-level copies.
- The active course initially mirrors the full 2025–26 structure. Do not
  proactively correct dates or academic-year references inside individual
  teaching documents; update them only when the user asks.
- After a course change, validate `config.yml`, commit it, and push `main`.
  The user may then need to click **Build/Rebuild** in the GitHub-connected
  Chirun package before the generated website changes.
- The 2025–26 reference build is:
  `https://lti.chirun.org.uk/media/chirun-packages/output/daf84705-b35e-4219-95a0-733823b1b1f6/index.html`.

