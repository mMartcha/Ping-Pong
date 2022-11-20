from cx_Freeze import setup, Executable

setup(name = "Ping Pong" ,
    version = "1.0" ,
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }},
    description = "Esse foi um projeto criado pelos alunos Henrique Tres Terra e Vinicius Artuso da instituição ATITUS, Passo Fundo" ,
    executables = [Executable("pingPong.py")])