srcdir  = '.'
blddir  = 'build'
VERSION = '1.0.0'

def set_options(ctx):
	ctx.tool_options('compiler_cxx')

def configure(ctx):
	ctx.check_tool('compiler_cxx')
	ctx.check_tool('node_addon')

def build(ctx):
	t1 = ctx.new_task_gen('cxx', 'shlib', 'node_addon')
	t1.target = 'profiler'
	t1.source = 'profiler.cc'  
	t2 = ctx.new_task_gen('cxx', 'shlib', 'node_addon')
	t2.target = 'd8compat'
	t2.source = 'd8-posix.cc'
