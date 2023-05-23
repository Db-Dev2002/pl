
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-left*/rightUMINUSNAME NUMBERstatement : NAME "=" expressionstatement : expressionexpression : expression \'+\' expression\n        | expression \'-\' expression\n        | expression \'*\' expression\n        | expression \'/\' expressionexpression : \'-\' expression %prec UMINUSexpression : \'(\' expression \')\'expression : NUMBERexpression : NAME'
    
_lr_action_items = {'NAME':([0,4,5,7,8,9,10,11,],[2,13,13,13,13,13,13,13,]),'-':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[4,-10,9,4,4,-9,4,4,4,4,4,-7,-10,9,9,-3,-4,-5,-6,-8,]),'(':([0,4,5,7,8,9,10,11,],[5,5,5,5,5,5,5,5,]),'NUMBER':([0,4,5,7,8,9,10,11,],[6,6,6,6,6,6,6,6,]),'$end':([1,2,3,6,12,13,15,16,17,18,19,20,],[0,-10,-2,-9,-7,-10,-1,-3,-4,-5,-6,-8,]),'=':([2,],[7,]),'+':([2,3,6,12,13,14,15,16,17,18,19,20,],[-10,8,-9,-7,-10,8,8,-3,-4,-5,-6,-8,]),'*':([2,3,6,12,13,14,15,16,17,18,19,20,],[-10,10,-9,-7,-10,10,10,10,10,-5,-6,-8,]),'/':([2,3,6,12,13,14,15,16,17,18,19,20,],[-10,11,-9,-7,-10,11,11,11,11,-5,-6,-8,]),')':([6,12,13,14,16,17,18,19,20,],[-9,-7,-10,20,-3,-4,-5,-6,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,7,8,9,10,11,],[3,12,14,15,16,17,18,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME = expression','statement',3,'p_statement_assign','grammar.py',24),
  ('statement -> expression','statement',1,'p_statement_expr','grammar.py',29),
  ('expression -> expression + expression','expression',3,'p_expression_binop','grammar.py',33),
  ('expression -> expression - expression','expression',3,'p_expression_binop','grammar.py',34),
  ('expression -> expression * expression','expression',3,'p_expression_binop','grammar.py',35),
  ('expression -> expression / expression','expression',3,'p_expression_binop','grammar.py',36),
  ('expression -> - expression','expression',2,'p_expression_uminus','grammar.py',40),
  ('expression -> ( expression )','expression',3,'p_expression_group','grammar.py',44),
  ('expression -> NUMBER','expression',1,'p_expression_number','grammar.py',48),
  ('expression -> NAME','expression',1,'p_expression_name','grammar.py',52),
]
