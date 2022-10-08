import sys
import configparser
from guizero import *
import subprocess
from PIL import Image
import os

argv = sys.argv
argc = len(sys.argv)
home_path = os.getenv("HOME")
mesaconfigur = configparser.ConfigParser()
mesaread = mesaconfigur.read(home_path+"/.thunder/mesa.cfg")
mesa32 = mesaconfigur.get("mesa","ARMHF")
mesa64 = mesaconfigur.get("mesa","ARM64")
mesaon = mesaconfigur.get("mesa","ON")
galliumon = mesaconfigur.get("mesa","GALLIUM_HUD")
gallium = open(home_path+"/.thunder/gallium.cfg", "r")
gallium_args = gallium.read()
gallium.close()

if argc == 2:
    global args
    global arguments
    args = ""
    arguments = ""
    if galliumon == "ON":
        args += " GALLIUM_HUD="+gallium_args+" "
    if mesaon == "1":
        args += " LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"+mesa64+":"+mesa32+" "
    configur = configparser.ConfigParser()
    configur.read(argv[1])
    name = configur.get("Game","NM")
    exec = configur.get("Game","ID")
    icon = configur.get("Game","CV")
    runner = configur.get("Game","RN")
    try:
        game_config_reader = configparser.ConfigParser()
        game_no_config = game_config_reader.read(home_path+"/.thunder/configs/"+name+".cfg")
        gl_switch = game_config_reader.get("Game Data","CONFIG_GL")
        if gl_switch == "ON":
            gl_data = game_config_reader.get("Game Data","CONFIG_GL_VERSION")
        env_switch = game_config_reader.get("Game Data","CONFIG_ENV")
        if env_switch == "ON":
            env_data = game_config_reader.get("Game Data","CONFIG_ENV_DATA")
        args_switch = game_config_reader.get("Game Data","CONFIG_ARGS")
        if args_switch == "ON":
            args_data = game_config_reader.get("Game Data","CONFIG_ARGS_DATA")
        game_config_read = True
    except:
        game_config_read = False
    if game_config_read == True:
        if gl_switch == "ON":
            args += " MESA_GL_VERSION_OVERRIDE="+gl_data+" "
        if env_switch == "ON":
            args += " "+env_data+" "
        if args_switch == "ON":
            arguments += " "+args_data+" "
    def gamerun():
        if runner == "linux":
            command = f''+args+' '+exec+' '+arguments
        if runner == "wine":
            command = f''+args+' wine '+exec+' '+arguments
        if runner == "steam":
            command = f''+args+' steam steam://rungameid/'+exec+' '+arguments
        if runner == "browser":
            command = f''+args+' x-www-browser '+exec+' '+arguments
        if runner == "flatpak":
            command = f''+args+' flatpak run '+exec+' '+arguments
        if runner == "mednafen":
            command = f''+args+' mednafen '+exec+' '+arguments
        process = subprocess.Popen(command, stderr=True, stdout=True, shell=True)
    def configure():
        global args
        def enable_box():
            if gl_version.value == "Default Version":
                custom_gl.enabled = False
                cgl.visible = False
            if gl_version.value == "Custom Version":
                custom_gl.enabled = True
                cgl.visible = True
        def enable_env():
            if env_var.value == "No Env. Variables":
                custom_env.enabled = False
                envy.visible = False
            if env_var.value == "Enter in Env. Variables":
                custom_env.enabled = True
                envy.visible = True
        def enable_arg():
            if any_args.value == "No Arguments":
                enter_args.enabled = False
                argsy.visible = False
            if any_args.value == "Enter in Arguments":
                enter_args.enabled = True
                argsy.visible = True
        def apply_config():
            global args
            if gl_version.value == "Default Version":
                config_gl = "OFF"
                config_gl_version = 0
            if gl_version.value == "Custom Version":
                config_gl = "ON"
                config_gl_version = custom_gl.value
            print("OpenGL: "+config_gl)
            if config_gl == "ON":
                print("Version: "+str(config_gl_version))
            if env_var.value == "No Env. Variables":
                config_env = "OFF"
                config_env_data = 0
            if env_var.value == "Enter in Env. Variables":
                config_env = "ON"
                config_env_data = custom_env.value
            print("Env. Variables: "+config_env)
            if config_env == "ON":
                print("Variable(s): "+str(config_env_data))
            if any_args.value == "No Arguments":
                config_args = "OFF"
                config_args_data = 0
            if any_args.value == "Enter in Arguments":
                config_args = "ON"
                config_args_data = enter_args.value
            print("Arguments: "+config_args)
            if config_args == "ON":
                print("Argument(s): "+str(config_args_data))
            if config_gl == "ON":
                args += " MESA_GL_VERSION_OVERRIDE="+str(config_gl_version)+" "
            if config_env == "ON":
                args += " "+str(config_env_data)+" "
            if config_args == "ON":
                arguments = " "+str(config_args_data)+" "
            game_config = open(home_path+"/.thunder/configs/"+name+".cfg","w")
            game_config.write("[Game Data]\n")
            game_config.write("CONFIG_GL = "+config_gl+"\n")
            game_config.write("CONFIG_GL_VERSION = "+str(config_gl_version)+"\n")
            game_config.write("CONFIG_ENV = "+config_env+"\n")
            game_config.write("CONFIG_ENV_DATA = "+str(config_env_data)+"\n")
            game_config.write("CONFIG_ARGS = "+config_args+"\n")
            game_config.write("CONFIG_ARGS_DATA = "+str(config_args_data)+"\n")
            game_config.close()
            info("Thunder - "+name+" - Configuration","Your configuration should now be applied. You may need to restart the cartridge.")
        configure = Window(app,title="Thunder - "+name+" - Configure",bg="white")
        Text(configure, text=name+" Configuration",size=20)
        Text(configure, text="OpenGL Version")
        gl_version = ButtonGroup(configure, options=["Default Version","Custom Version"],selected="Default Version",command=enable_box)
        cgl = Text(configure, text="Example: 3.3")
        custom_gl = TextBox(configure,text="Enter custom version here...",width=25)
        if gl_version.value == "Default Version":
            custom_gl.enabled = False
            cgl.visible = False
        Text(configure, text="Environment Variables")
        env_var = ButtonGroup(configure, options=["No Env. Variables","Enter in Env. Variables"],selected="No Env. Variables",command=enable_env)
        envy = Text(configure, text="Example: LD_LIBRARY_PATH=/home/pi/lib")
        custom_env = TextBox(configure,text="Enter env. variables here...",width=25)
        if env_var.value == "No Env. Variables":
            custom_env.enabled = False
            envy.visible = False
        Text(configure, text="Arguments")
        any_args = ButtonGroup(configure, options=["No Arguments","Enter in Arguments"],selected="No Arguments",command=enable_arg)
        argsy = Text(configure, text="Example: --fullscreen")
        enter_args = TextBox(configure,text="Enter in arguments here...",width=25)
        if any_args.value == "No Arguments":
            enter_args.enabled = False
            argsy.visible = False
        PushButton(configure,text="Apply Configuration",align="bottom",command=apply_config)
        configure.update()
    app = App(title="Thunder - "+name, width=600,bg="white")
    app.icon = icon
    PushButton(app,text="Run Game...",command=gamerun,align="bottom")
    PushButton(app,text="Configure...",command=configure,align="bottom")
    cover = Image.open(icon)
    cover_pic = Picture(app, image=cover, align="top", height=308, width=220)
    Text(app, text=name)
    Text(app, text="Platform: "+runner)
    app.display()
    print("\n")
