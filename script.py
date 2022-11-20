from cx_Freeze import setup, Executable

setup(name = "Ping Pong" ,
    version = "1.0" ,
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }},
    description = "Esse foi um projeto criado pelos alunos Marcello Stefenon Filho e Guilherme Almeida Franciosi da instituição ATITUS, Passo Fundo" ,
    executables = [Executable("pingPong.py")])