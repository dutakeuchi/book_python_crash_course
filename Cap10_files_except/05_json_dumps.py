# %%
from pathlib import Path
import json
# %%
numbers = input('digit anything')
path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
# %%
