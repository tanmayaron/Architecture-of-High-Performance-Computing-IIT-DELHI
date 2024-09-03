from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import Resource
from gem5.resources.resource import CustomResource
from gem5.simulate.simulator import Simulator

cache_hierarchy = NoCache()

memory = SingleChannelDDR3_1600("1GiB")

processor = SimpleProcessor(cpu_type=CPUTypes.KVM, num_cores=1)


board = SimpleBoard(	    
	    clk_freq="2GHz",
	    processor=processor,
	    memory=memory,
	    cache_hierarchy=cache_hierarchy,
)

binary = CustomResource("./HPC1/mm")
board.set_se_binary_workload(binary)

simulator = Simulator(board=board)
simulator.run()