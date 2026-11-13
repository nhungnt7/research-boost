import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    result = importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

installer, brief = module('install'), module('new_brief')

class Helpers(unittest.TestCase):
    def test_install_is_complete_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder)/'project/.agents/skills/research-boost'
            installer.install(ROOT/'skills/research-boost',dest)
            config = json.loads((dest/'artifact-template.json').read_text())
            self.assertTrue((dest/config['reference']).is_file())
            original = (dest/'SKILL.md').read_bytes()
            with self.assertRaises(FileExistsError):installer.install(ROOT/'skills/research-boost',dest)
            self.assertEqual(original,(dest/'SKILL.md').read_bytes())

    def test_all_seed_modes_round_trip_without_research(self):
        with tempfile.TemporaryDirectory() as folder:
            for mode in brief.MODES:
                dest = Path(folder)/mode
                brief.create_brief(dest,mode,'Robot teams',['one source','another source'],
                                   'ML researchers',25,'2020-2026','2026-11-13')
                saved = json.loads((dest/'brief.json').read_text())
                self.assertEqual(saved['mode'],mode)
                self.assertEqual(saved['seeds'],['one source','another source'])
                self.assertIn('$research-boost',(dest/'prompt.txt').read_text())
                with self.assertRaises(FileExistsError):
                    brief.create_brief(dest,mode,'Robot teams',['seed'],'Researchers',25,'','2026-11-13')

if __name__ == '__main__':unittest.main()
