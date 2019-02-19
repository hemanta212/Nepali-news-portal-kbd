'''Simplify logging creation no needed parameter '''
import logging

class Logger:
    '''
    Customized logger class having get_logger method returning a logger
    params:
        name = filename to pass generally it is __name__
        (opt)level = specify level for filehandler (Warning is default)
        (opt)file = file to write log messages to (project.log is default)
        (opt)debug_file = specify debug_on file (sets debug_on automatically)
        (opt)multidebug if true writes to debug_file in append mode.
        
    '''
    def __init__(self, name=None, level=logging.DEBUG, file='project.log',
                    debug_on=False, debug_file='debug.log'):
        self.name = name
        self.level = level
        self.file = file
        self.debug_on = debug_on
        self.debug_file = debug_file

    def get_logger(self):
        '''returns a logger as specified in Logger class'''
        if self.name is None:
            import inspect
            caller = inspect.currentframe().f_back
            self.name = caller.f_globals['__name__']

        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        # create formatter
        format_style = '%(asctime)s : %(name)s: %(levelname)s : %(message)s'
        formatter = logging.Formatter(format_style)
        # add formatter to console_handler
        console_handler.setFormatter(formatter)
        # add console_handler to logger
        logger.addHandler(console_handler)

        #create file handler and set level to warning
        if self.file == 'project.log': #since project.log is default.
            filehandler = logging.FileHandler(self.file, mode='a')
        else:
            filehandler = logging.FileHandler(self.file, mode='w')
        filehandler.setLevel(logging.WARNING)
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        if (self.debug_on == True or self.debug_file != 'debug.log'):
            #create file handler and set level to warning
            debug_filehandler = logging.FileHandler(self.debug_file, mode='w')
            debug_filehandler.setLevel(logging.DEBUG)
            debug_filehandler.setFormatter(formatter)
            logger.addHandler(debug_filehandler)
        return logger
