#!/usr/bin/env python
# -*- coding: utf-8 -*-

from module.dependency import Dependency

class Caller(object):
    def __init__(self):
        self.depend = Dependency()
    
    def call_dependency(self, filename):
        self.depend.rm(filename)


class CallerTwo(object):
    def call_dependency(self, filename):
        Dependency().rm(filename)


