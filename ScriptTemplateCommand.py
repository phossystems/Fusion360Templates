#Author-Author
#Description-Description

import adsk.core, adsk.fusion, adsk.cam, traceback


# Global set of event handlers to keep them referenced for the duration of the command
_handlers = []

# TODO: Chage to unique values 
COMMAND_ID = "commandId"


# Fires when the CommandDefinition gets executed.
# Responsible for adding commandInputs to the command &
# registering the other command handlers.
class CommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # Get the command that was created.
            cmd = adsk.core.Command.cast(args.command)

            # Some common EventHandlers
            # For more Handlers and Info go to:
            # http://help.autodesk.com/view/fusion360/ENU/?guid=GUID-3922697A-7BF1-4799-9A5B-C8539DF57051

            # Registers the CommandDestryHandler
            onExecute = CommandExecuteHandler()
            cmd.execute.add(onExecute)
            _handlers.append(onExecute)  
            
            # Registers the CommandExecutePreviewHandler
            onExecutePreview = CommandExecutePreviewHandler()
            cmd.executePreview.add(onExecutePreview)
            _handlers.append(onExecutePreview)
            
            # Registers the CommandInputChangedHandler          
            onInputChanged = CommandInputChangedHandler()
            cmd.inputChanged.add(onInputChanged)
            _handlers.append(onInputChanged)            
            
            # Registers the CommandDestryHandler
            onDestroy = CommandDestroyHandler()
            cmd.destroy.add(onDestroy)
            _handlers.append(onDestroy)

                
            # Get the CommandInputs collection associated with the command.
            inputs = cmd.commandInputs
            
            # TODO: Add CommandInputs here
            inputs.addTextBoxCommandInput("id","Name","Hello World!", 1, False)

           
        except:
            print(traceback.format_exc())




#Fires when the User executes the Command
#Responsible for doing the changes to the document
class CommandExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            print("execute")
            # TODO: Add Command Execution Stuf Here
            pass                
            
        except:
            print(traceback.format_exc())




# Fires when the Command is being created or when Inputs are being changed
# Responsible for generating a preview of the output.
# Changes done here are temporary and will be cleaned up automatically.
class CommandExecutePreviewHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            eventArgs = adsk.core.CommandEventArgs.cast(args)
            
            # TODO: Add Command Execution Preview Stuff Here
            
            # If set to True Fusion will use the last preview instead of calling
            # the ExecuteHandler when the user executes the Command.
            # If the preview is identical to the actual executing this saves recomputation
            eventArgs.isValidResult = False                
            
        except:
            print(traceback.format_exc())



# Fires when CommandInputs are changed
# Responsible for dynamically updating other Command Inputs
class CommandInputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # TODO: Add Input Changed Stuff Here
            pass
        except:
            print(traceback.format_exc())
                
                
                
# Fires when the Command gets Destroyed regardless of success
# Responsible for cleaning up                 
class CommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # When the command is done, terminate the script
            # This will release all globals which will remove all event handlers
            adsk.terminate()
        except:
            print(traceback.format_exc())




def run(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        
        commandDefinitions = ui.commandDefinitions
        #check the command exists or not
        cmdDef = commandDefinitions.itemById(COMMAND_ID)
        if not cmdDef:
            cmdDef = commandDefinitions.addButtonDefinition(COMMAND_ID, COMMAND_ID,
                                                            COMMAND_ID, '')
        onCommandCreated = CommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        _handlers.append(onCommandCreated)
        inputs = adsk.core.NamedValues.create()
        cmdDef.execute(inputs)

        # prevent this module from being terminate when the script returns, because we are waiting for event handlers to fire
        adsk.autoTerminate(False)
    except:
        print(traceback.format_exc())
