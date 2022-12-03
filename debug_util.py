from collections import defaultdict
import json


class Memo:
    def __init__(self) -> None:
        self.data = {}
        self.get_records = defaultdict(int)
        self.check_records = defaultdict(int)
        self.set_records = defaultdict(int)

    def __getitem__(self, key):
        self.get_records[str(key)] += 1
        return self.data[key]

    def __setitem__(self, key, value):
        self.set_records[str(key)] += 1
        self.data[key] = value

    def __contains__(self, key):
        self.check_records[str(key)] += 1
        return key in self.data

    def dump(self, prefix: str = ''):
        for i in 'check get set'.split():
            name = f'{i}_records'
            with open(f'{prefix}_{name}.json', 'w') as f:
                records = getattr(self, name)
                records['all'] = sum(records.values())
                json.dump(records, f, indent=2)


class DefaultMemo(Memo):
    def __init__(self, default_value) -> None:
        super().__init__()
        self.data = defaultdict(lambda : default_value)