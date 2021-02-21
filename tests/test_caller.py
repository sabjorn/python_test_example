#!/usr/bin/env python
# -*- coding: utf-8 -*-

from module import (Caller, CallerTwo, Dependency)

import mock
import unittest

class CallerTestCase(unittest.TestCase):
    @mock.patch.object(Dependency, 'rm')
    def test_call_dependency(self, mock_rm):
        # build our dependencies
        reference = Caller()
        
        # call upload_complete, which should, in turn, call `rm`:
        reference.call_dependency("my uploaded file")
        
        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")

class CallerTwoTestCase(unittest.TestCase):
    @mock.patch.object(Dependency, 'rm')
    def test_call_dependency(self, mock_rm):
        # build our dependencies
        reference = CallerTwo()
        
        # call upload_complete, which should, in turn, call `rm`:
        reference.call_dependency("my uploaded file")
        
        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")


if __name__ == '__main__':
    unittest.main()
