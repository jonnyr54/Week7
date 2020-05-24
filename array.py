from adts.iarray import IArray


class Array(IArray):
    def __init__(self, size):
        raise NotImplementedError()

    def clone(instance):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __setitem__(self, index, data):
        raise NotImplementedError()

    def __len__(self) -> int:
        raise NotImplementedError()

    def resize(self, new_size):
        raise NotImplementedError()

    def __eq__(self, other) -> bool:
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __delitem__(self, index):
        raise NotImplementedError()

    def __contains__(self, item) -> bool:
        raise NotImplementedError()
