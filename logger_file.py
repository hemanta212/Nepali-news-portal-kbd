'''Simplify logging creation no needed parameter '''
import logging
import os

class Logger:
    '''
    Customized logger class having get_logger method returning a logger
    params:
        (opt)name = filename to pass generally it is __name__
        (opt)level = specify level for Hfilehandler (Warning is default)
        (opt)file = file to write log messages to (project.log is default)
        (opt)mode = which mode to write. Default['a']
        (opt)debug_file = specify mode file
        (opt)debug_mode = specify which mode to use default['w']
    '''
    def __init__(self, name=None, level='warning', file='project.log',
                    mode='a', debug_file=None, debug_mode='w', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.level = self.level_parser(level)
        self.file = file
        self.mode = mode
        self.debug_mode = debug_mode
        self.debug_file = debug_file

    @staticmethod
    def level_parser(key):
        level_dict = {
            'debug':logging.DEBUG,
            'warning':logging.WARNING,
            'error':logging.ERROR,
            'info':logging.INFO,
            'fatal':logging.FATAL,
            'critical':logging.CRITICAL,
        }
        return level_dict[key]
    @staticmethod
    def handle_file(file):
        '''
        Checks if a file exists if not creates directory upto that files
        Params:
            file : Input file
        '''
        if not os.path.exists(file):
            try:
                os.makedirs(os.path.split(file)[0])
            except FileExistsError:
                pass

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
            filehandler = logging.FileHandler(self.file, mode=self.mode)
        else:
            self.handle_file(self.file)
            filehandler = logging.FileHandler(self.file, mode=self.mode)
        filehandler.setLevel(self.level)
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        if self.debug_file:
            self.handle_file(self.debug_file)
            debug_filehandler = logging.FileHandler(self.debug_file, mode=self.debug_mode)
            debug_filehandler.setLevel(logging.DEBUG)
            debug_filehandler.setFormatter(formatter)
            logger.addHandler(debug_filehandler)
        return logger
