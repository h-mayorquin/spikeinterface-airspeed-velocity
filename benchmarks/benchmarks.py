# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.
import tempfile


class IoSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        from spikeinterface.core import generate_recording
        
        self.recording = generate_recording(num_channels=384, durations=[1.0])
        
    def time_write_binary(self):
        from spikeinterface.core import write_binary_recording
        
        with tempfile.TemporaryDirectory() as temp_dir:
            write_binary_recording(recording=self.recording, save_path=temp_dir)
        


# class MemSuite:
#     def mem_list(self):
#         return [0] * 256
