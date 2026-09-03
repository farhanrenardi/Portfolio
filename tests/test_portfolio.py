"""Automated verification test suite for Farhan Faiq's portfolio.

Covers environment sanity, asset existence, zero unicode emojis,
recruiter-first projects, hero identity, technical stack icons, and README alignment.
"""

from pathlib import Path
import re
import unittest

BASE_DIR = Path(__file__).resolve().parent.parent

# Comprehensive regex range for Unicode emojis
EMOJI_PATTERN = re.compile(
    r"["
    r"\U0001F600-\U0001F64F"  # Emoticons
    r"\U0001F300-\U0001F5FF"  # Misc Symbols and Pictographs
    r"\U0001F680-\U0001F6FF"  # Transport and Map
    r"\U0001F700-\U0001F77F"  # Alchemical Symbols
    r"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    r"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    r"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    r"\U0001FA00-\U0001FA6F"  # Chess Symbols
    r"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    r"\U00002600-\U000026FF"  # Misc Symbols
    r"\U00002700-\U000027BF"  # Dingbats
    r"\U0001F1E6-\U0001F1FF"  # Enclosed Alphanumeric Supplement / Flags
    r"]",
    flags=re.UNICODE,
)


class TestPortfolio(unittest.TestCase):
    """Test suite verifying portfolio assets, content, and quality gates."""

    def setUp(self):
        self.index_path = BASE_DIR / "index.html"
        self.readme_path = BASE_DIR / "README.md"

    def test_test_environment_sanity(self):
        """Checks index.html and README.md exist on disk and are non-empty."""
        self.assertTrue(self.index_path.is_file(), "index.html does not exist on disk")
        self.assertGreater(
            self.index_path.stat().st_size, 0, "index.html exists but is empty"
        )
        self.assertTrue(self.readme_path.is_file(), "README.md does not exist on disk")
        self.assertGreater(
            self.readme_path.stat().st_size, 0, "README.md exists but is empty"
        )

    def test_zero_unicode_emojis(self):
        """Audits index.html and README.md to assert that zero unicode emojis exist."""
        index_content = self.index_path.read_text(encoding="utf-8")
        readme_content = self.readme_path.read_text(encoding="utf-8")

        html_emojis = EMOJI_PATTERN.findall(index_content)
        readme_emojis = EMOJI_PATTERN.findall(readme_content)

        self.assertEqual(
            len(html_emojis),
            0,
            f"Found unicode emojis in index.html: {html_emojis}",
        )
        self.assertEqual(
            len(readme_emojis),
            0,
            f"Found unicode emojis in README.md: {readme_emojis}",
        )

    def test_physical_assets_exist(self):
        """Asserts that CV PDF, snapshot assets, and DataOps artifacts exist on disk."""
        cv_path = BASE_DIR / "assets" / "CV_Farhan Faiq.pdf"
        self.assertTrue(cv_path.is_file(), f"CV not found at: {cv_path}")
        self.assertGreater(cv_path.stat().st_size, 0, f"CV is empty at: {cv_path}")

        snapshots_dir = BASE_DIR / "assets" / "snapshots"
        required_snapshots = [
            "snapshot1.mp4",
            "snapshot1.png",
            "snapshot2.mp4",
            "snapshot2.png",
            "snapshot6.mp4",
            "snapshot6.png",
        ]
        for snapshot_file in required_snapshots:
            snapshot_path = snapshots_dir / snapshot_file
            self.assertTrue(
                snapshot_path.is_file(),
                f"Required snapshot asset not found at: {snapshot_path}",
            )

        canvas_path = BASE_DIR / "assets" / "agentic_dataops_canvas.png"
        self.assertTrue(canvas_path.is_file(), f"Agentic DataOps canvas not found at: {canvas_path}")
        self.assertGreater(canvas_path.stat().st_size, 0, f"Agentic DataOps canvas is empty at: {canvas_path}")

        pipeline_json_path = BASE_DIR / "assets" / "Agentic_DataOps_Capstone.json"
        self.assertTrue(pipeline_json_path.is_file(), f"Pipeline JSON not found at: {pipeline_json_path}")
        self.assertGreater(pipeline_json_path.stat().st_size, 0, f"Pipeline JSON is empty at: {pipeline_json_path}")

        dbt_icon_path = BASE_DIR / "assets" / "dbt.svg"
        self.assertTrue(dbt_icon_path.is_file(), f"dbt SVG icon not found at: {dbt_icon_path}")
        self.assertGreater(dbt_icon_path.stat().st_size, 0, f"dbt SVG icon is empty at: {dbt_icon_path}")

    def test_hero_and_identity(self):
        """Asserts hero title/meta and typewriter words establish AI & Data Engineer identity."""
        index_content = self.index_path.read_text(encoding="utf-8")

        og_pattern = r'<meta property="og:title" content="[^"]*AI (&|&amp;) Data Engineer[^"]*">'
        og_match = re.search(og_pattern, index_content, re.IGNORECASE)
        has_identity = (
            og_match is not None
            or bool(re.search(r'<meta\s+property="og:title"\s+content="[^"]*AI\s+(&|&amp;)\s+Data Engineer[^"]*"', index_content, re.IGNORECASE))
            or bool(re.search(r'<title>[^<]*AI\s+(&|&amp;)\s+Data Engineer[^<]*</title>', index_content, re.IGNORECASE))
            or "AI & Data Engineer" in index_content
        )
        self.assertTrue(
            has_identity,
            "index.html title or og:title does not contain or match 'AI & Data Engineer'",
        )

        tw_match = re.search(r"const\s+twWords\s*=\s*\[(.*?)\];", index_content, re.DOTALL)
        self.assertIsNotNone(tw_match, "twWords array not found in index.html")
        tw_content = tw_match.group(1)
        self.assertTrue(
            "AI & Data Engineer" in tw_content or "AI &amp; Data Engineer" in tw_content,
            "twWords array does not contain 'AI & Data Engineer'",
        )

    def test_recruiter_first_projects(self):
        """Asserts index.html references top projects, documentation links, and snapshot videos."""
        index_content = self.index_path.read_text(encoding="utf-8")

        self.assertIn(
            "https://farhanrenardi.github.io/LogistiQ/",
            index_content,
            "index.html does not reference LogistiQ documentation URL",
        )
        self.assertIn(
            "https://farhanrenardi.github.io/-worka-jobmapper_and_scraper/",
            index_content,
            "index.html does not reference Worka 2.0 documentation URL",
        )
        self.assertIn(
            "Agentic DataOps",
            index_content,
            "index.html does not reference Agentic DataOps",
        )

        for video_tag in ["snapshot1.mp4", "snapshot2.mp4", "snapshot6.mp4"]:
            self.assertIn(
                video_tag,
                index_content,
                f"index.html does not contain snapshot video reference: {video_tag}",
            )

        self.assertTrue(
            "dataopsFlowModal" in index_content or "agentic_dataops_canvas.png" in index_content,
            "index.html does not reference dataopsFlowModal or agentic_dataops_canvas.png",
        )
        self.assertIn(
            "Agentic_DataOps_Capstone.json",
            index_content,
            "index.html does not reference Agentic_DataOps_Capstone.json",
        )

    def test_technical_stack_svgs(self):
        """Asserts index.html references key modern tech stack skills and icon presentation."""
        index_content = self.index_path.read_text(encoding="utf-8")

        for tech in ["PostgreSQL", "pgvector", "FastAPI", "Docker"]:
            self.assertIn(
                tech.lower(),
                index_content.lower(),
                f"Missing technology reference in index.html: {tech}",
            )

        self.assertTrue(
            "dbt core" in index_content.lower() or "dbt" in index_content.lower(),
            "Missing dbt Core technology reference in index.html",
        )
        self.assertTrue(
            "gemini" in index_content.lower() or "google genai" in index_content.lower(),
            "Missing Gemini / Google GenAI technology reference in index.html",
        )

        has_icon_elements = (
            "slide-icon-img" in index_content
            or "<svg" in index_content
            or "devicon" in index_content
        )
        self.assertTrue(
            has_icon_elements,
            "index.html does not use .slide-icon-img, SVG, or devicon elements for icons",
        )

    def test_readme_alignment(self):
        """Asserts README.md aligns with AI & Data Engineer positioning without emojis."""
        readme_content = self.readme_path.read_text(encoding="utf-8")

        self.assertTrue(
            "AI & Data Engineer" in readme_content or "AI &amp; Data Engineer" in readme_content,
            "README.md does not contain 'AI & Data Engineer'",
        )
        self.assertIn(
            "LogistiQ",
            readme_content,
            "README.md does not reference LogistiQ",
        )
        self.assertIn(
            "Worka",
            readme_content,
            "README.md does not reference Worka",
        )

        readme_emojis = EMOJI_PATTERN.findall(readme_content)
        self.assertEqual(
            len(readme_emojis),
            0,
            f"README.md contains unicode emojis: {readme_emojis}",
        )


if __name__ == "__main__":
    unittest.main()
