import cx_Freeze

executables= [cx_Freeze.Executable("cargame1.py")]
cx_Freeze.setup(
    name="A car game",
    options={"build_exe": {"packages":["pygame","time","random"],"include_files":["car.png"]}},
    executables = executables
    )
