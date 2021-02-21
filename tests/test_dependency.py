#!/usr/bin/env python
# -*- coding: utf-8 -*-

import module

import mock
import unittest

class DependencyTestCase(unittest.TestCase):

    @mock.patch('module.dependency.os', autospec=True)
    def test_rm_file_exists(self, mock_os):
        # set mock behaviour
        mock_os.path.isfile.return_value = True

        # build our dependencies
        reference = module.Dependency()
        
        # call upload_complete, which should, in turn, call `rm`:
        reference.rm("my uploaded file")
        
        # check that it called the rm method of any RemovalService
        mock_os.remove.assert_called_with("my uploaded file")
    
    @mock.patch('module.dependency.os', autospec=True)
    def test_rm_file_not_exists(self, mock_os):
        mock_os.path.isfile.return_value = False

        reference = module.Dependency()
        reference.rm("my uploaded file")
        
        mock_os.remove.assert_not_called()

if __name__ == '__main__':
    unittest.main()