
from abc import ABC, abstractmethod
from typing import List

from .tcx import tcxfile

class SamplingStrategy(ABC):

    @abstractmethod
    def migrate(self, src, dst) -> List:
        pass


class DataMigrationContext:
    def __init__(self, src: tcxfile.TCXFile, dst: tcxfile.TCXFile, sampling_strategy: SamplingStrategy = None, metric = None):
        self._src = src
        self._dst = dst
        self._metric = metric if metric is not None else 'HR'

        # improve flexibility to other sampling techniques here
        self._strategy = TrackpointIndexStrategy()

    def migrate(self):
        # improve flexibility to other metrics here
        if self._metric != 'HR':
            return

        src_data = self._src.extract_heart_rate()
        dst_data = self._dst.extract_heart_rate()

        self._strategy.migrate(src_data, dst_data)

        # improve flexibility to other metrics here
        self._dst.update_heart_rate_data(dst_data)


class TrackpointIndexStrategy(SamplingStrategy):
    def migrate(self, src, dst) -> List:
        print("Migrating with " + str(__class__))

        if len(src) >= len(dst):
            return src[:len(dst)]
        else:
            r =  src + dst[len(src):]
            return r

        print("HR Samples - src: " + str(len(src)) + " dst: " + str(len(dst)))
