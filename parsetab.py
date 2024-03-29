
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLIENT CONNECT CREATE DATA DELETE EQUALS INFO INT SEND SERVER STRINGstatement : CREATE CLIENT STRING\n                 | DELETE STRING\n    statement : CREATE SERVER STRING DATA INT\n                 | CREATE SERVER STRING STRING INT\n                 | CREATE SERVER STRING\n    statement : INFO STRINGstatement : STRING EQUALS DATAstatement : STRING EQUALS INTstatement : STRING SEND STRING DATA\n                 | STRING SEND STRING STRING\n    statement : STRING CONNECT STRINGstatement : STRING CONNECT DATA'
    
_lr_action_items = {'CREATE':([0,],[2,]),'DELETE':([0,],[4,]),'INFO':([0,],[5,]),'STRING':([0,4,5,6,7,9,10,14,17,],[3,11,12,13,14,17,18,20,22,]),'$end':([1,11,12,13,14,15,16,18,19,22,23,24,25,],[0,-2,-6,-1,-5,-7,-8,-11,-12,-10,-9,-4,-3,]),'CLIENT':([2,],[6,]),'SERVER':([2,],[7,]),'EQUALS':([3,],[8,]),'SEND':([3,],[9,]),'CONNECT':([3,],[10,]),'DATA':([8,10,14,17,],[15,19,21,23,]),'INT':([8,20,21,],[16,24,25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> CREATE CLIENT STRING','statement',3,'p_statement_create_or_delete_client_server','main.py',57),
  ('statement -> DELETE STRING','statement',2,'p_statement_create_or_delete_client_server','main.py',58),
  ('statement -> CREATE SERVER STRING DATA INT','statement',5,'p_statement_create_server','main.py',71),
  ('statement -> CREATE SERVER STRING STRING INT','statement',5,'p_statement_create_server','main.py',72),
  ('statement -> CREATE SERVER STRING','statement',3,'p_statement_create_server','main.py',73),
  ('statement -> INFO STRING','statement',2,'p_statement_info','main.py',89),
  ('statement -> STRING EQUALS DATA','statement',3,'p_statement_variable_string','main.py',98),
  ('statement -> STRING EQUALS INT','statement',3,'p_statement_variable_int','main.py',103),
  ('statement -> STRING SEND STRING DATA','statement',4,'p_statement_send_data','main.py',108),
  ('statement -> STRING SEND STRING STRING','statement',4,'p_statement_send_data','main.py',109),
  ('statement -> STRING CONNECT STRING','statement',3,'p_statement_local_conn','main.py',118),
  ('statement -> STRING CONNECT DATA','statement',3,'p_statement_external_conn_no_port','main.py',135),
]
