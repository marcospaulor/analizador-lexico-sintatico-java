
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOLEAN CLASS COMMA DIVIDE DOT ELSE EQUAL EQUALS EXTENDS FALSE FOR GREATER_THAN GREATER_THAN_OR_EQUAL ID IF IMPORT INT INT_LITERAL LBRACE LESS_THAN LESS_THAN_OR_EQUAL LPAREN LSQUARE MAIN MINUS MINUS_MINUS NEW NOT NOT_EQUALS OR OUT PLUS PLUS_PLUS PRINTLN PRIVATE PROTECTED PUBLIC RBRACE RETURN RPAREN RSQUARE SEMICOLON STATIC STRING STRING_LITERAL SYSTEM THIS TIMES TRUE VOID WHILE\n            program : body_program\n        \n            body_program : class_decl body_program\n                | import_decl body_program\n                | var_decl body_program\n                | empty\n        \n            class_decl : CLASS ID EXTENDS ID LBRACE body RBRACE\n                | CLASS ID LBRACE body RBRACE\n                | access_modifier CLASS ID EXTENDS ID LBRACE body RBRACE\n                | access_modifier CLASS ID LBRACE body RBRACE\n        \n            access_modifier : PUBLIC\n                | PRIVATE\n                | PROTECTED\n        \n            import_decl : IMPORT ID DOT ID SEMICOLON\n                | IMPORT ID DOT ID DOT ID SEMICOLON\n        \n            var_decl : type ID SEMICOLON\n                | type ID EQUAL expr SEMICOLON\n        \n            method_decl : type ID LPAREN params RPAREN LBRACE body RBRACE\n                        | access_modifier type ID LPAREN params RPAREN LBRACE body RBRACE\n                        | type ID LPAREN RPAREN LBRACE body RBRACE\n                        | access_modifier STATIC type ID LPAREN params RPAREN LBRACE body RBRACE\n                        | PUBLIC STATIC VOID MAIN LPAREN params RPAREN LBRACE body RBRACE\n        \n            params : type ID\n                | type ID COMMA params\n                | empty\n        \n            body : var_decl body\n                | method_decl body\n                | statement body\n                | empty\n        \n            type : INT\n                | BOOLEAN\n                | STRING\n                | ID\n                | VOID\n                | type LSQUARE RSQUARE\n        \n            expr : expr PLUS term\n                | expr MINUS term\n                | expr AND term\n                | expr OR term\n                | expr EQUALS term\n                | expr NOT_EQUALS term\n                | expr LESS_THAN term\n                | expr LESS_THAN_OR_EQUAL term\n                | expr GREATER_THAN term\n                | expr GREATER_THAN_OR_EQUAL term\n                | term\n        \n            term : term TIMES factor\n                | term DIVIDE factor\n                | factor\n        \n            factor : MINUS factor\n                | NOT factor\n                | INT_LITERAL\n                | TRUE\n                | FALSE\n                | STRING_LITERAL\n                | ID\n                | ID LSQUARE expr RSQUARE\n                | ID DOT ID\n                | ID DOT ID LPAREN args RPAREN\n                | ID LPAREN args RPAREN\n                | NEW ID LPAREN RPAREN\n                | NEW INT LSQUARE expr RSQUARE\n                | LPAREN expr RPAREN\n        \n            args : expr\n                | expr COMMA args\n                | empty\n        \n            for_loop : FOR LPAREN var_decl expr SEMICOLON assign_expr RPAREN statement\n                    | FOR LPAREN SEMICOLON expr SEMICOLON assign_expr RPAREN statement\n                    | FOR LPAREN var_decl expr SEMICOLON increment_expr RPAREN statement\n                    | FOR LPAREN SEMICOLON expr SEMICOLON increment_expr RPAREN statement\n        \n            assign_expr : ID EQUALS expr\n        \n            increment_expr : ID PLUS_PLUS\n                        | ID MINUS_MINUS\n                        | PLUS_PLUS ID\n                        | MINUS_MINUS ID\n        \n            statement : LBRACE body RBRACE\n                | IF LPAREN expr RPAREN statement ELSE statement\n                | IF LPAREN expr RPAREN statement\n                | WHILE LPAREN expr RPAREN statement\n                | SYSTEM DOT OUT DOT PRINTLN LPAREN expr RPAREN SEMICOLON\n                | ID EQUALS expr SEMICOLON\n                | ID LSQUARE expr RSQUARE EQUALS expr SEMICOLON\n                | ID DOT ID EQUALS expr SEMICOLON\n                | ID DOT ID LPAREN args RPAREN SEMICOLON\n                | ID LPAREN args RPAREN SEMICOLON\n                | RETURN expr SEMICOLON\n                | RETURN SEMICOLON\n                | ID PLUS_PLUS SEMICOLON\n                | ID MINUS_MINUS SEMICOLON\n                | PLUS_PLUS ID SEMICOLON\n                | MINUS_MINUS ID SEMICOLON\n                | THIS DOT ID EQUAL expr SEMICOLON\n                | THIS DOT ID LPAREN args RPAREN SEMICOLON\n                | for_loop\n        empty :'
    
_lr_action_items = {'CLASS':([0,3,4,5,9,12,13,14,31,77,97,101,143,163,185,210,],[7,7,7,7,23,-10,-11,-12,-15,-7,-13,-16,-9,-6,-14,-8,]),'IMPORT':([0,3,4,5,31,77,97,101,143,163,185,210,],[10,10,10,10,-15,-7,-13,-16,-9,-6,-14,-8,]),'$end':([0,1,2,3,4,5,6,19,20,21,31,77,97,101,143,163,185,210,],[-94,0,-1,-94,-94,-94,-5,-2,-3,-4,-15,-7,-13,-16,-9,-6,-14,-8,]),'PUBLIC':([0,3,4,5,28,31,36,38,39,40,52,55,69,77,89,97,101,126,127,128,136,137,138,142,143,163,164,185,194,198,202,204,210,214,217,224,234,235,238,239,242,244,254,256,257,259,260,262,263,264,267,268,269,],[12,12,12,12,44,-15,44,44,44,44,-93,44,44,-7,-86,-13,-16,-87,-88,-75,-85,-89,-90,44,-9,-6,-80,-14,-84,44,-77,-78,-8,-82,44,-91,-81,-83,-19,44,-76,-92,-17,44,44,-66,-68,-67,-69,-18,-79,-20,-21,]),'PRIVATE':([0,3,4,5,28,31,36,38,39,40,52,55,69,77,89,97,101,126,127,128,136,137,138,142,143,163,164,185,194,198,202,204,210,214,217,224,234,235,238,239,242,244,254,256,257,259,260,262,263,264,267,268,269,],[13,13,13,13,13,-15,13,13,13,13,-93,13,13,-7,-86,-13,-16,-87,-88,-75,-85,-89,-90,13,-9,-6,-80,-14,-84,13,-77,-78,-8,-82,13,-91,-81,-83,-19,13,-76,-92,-17,13,13,-66,-68,-67,-69,-18,-79,-20,-21,]),'PROTECTED':([0,3,4,5,28,31,36,38,39,40,52,55,69,77,89,97,101,126,127,128,136,137,138,142,143,163,164,185,194,198,202,204,210,214,217,224,234,235,238,239,242,244,254,256,257,259,260,262,263,264,267,268,269,],[14,14,14,14,14,-15,14,14,14,14,-93,14,14,-7,-86,-13,-16,-87,-88,-75,-85,-89,-90,14,-9,-6,-80,-14,-84,14,-77,-78,-8,-82,14,-91,-81,-83,-19,14,-76,-92,-17,14,14,-66,-68,-67,-69,-18,-79,-20,-21,]),'INT':([0,3,4,5,13,14,28,31,36,38,39,40,43,44,52,55,68,69,77,83,89,93,97,101,126,127,128,129,136,137,138,142,143,163,164,174,185,194,198,200,201,202,204,210,214,216,217,224,234,235,238,239,242,244,254,256,257,259,260,262,263,264,267,268,269,],[15,15,15,15,-11,-12,15,-15,15,15,15,15,15,-10,-93,15,118,15,-7,15,-86,15,-13,-16,-87,-88,-75,15,-85,-89,-90,15,-9,-6,-80,15,-14,-84,15,15,15,-77,-78,-8,-82,15,15,-91,-81,-83,-19,15,-76,-92,-17,15,15,-66,-68,-67,-69,-18,-79,-20,-21,]),'BOOLEAN':([0,3,4,5,13,14,28,31,36,38,39,40,43,44,52,55,69,77,83,89,93,97,101,126,127,128,129,136,137,138,142,143,163,164,174,185,194,198,200,201,202,204,210,214,216,217,224,234,235,238,239,242,244,254,256,257,259,260,262,263,264,267,268,269,],[16,16,16,16,-11,-12,16,-15,16,16,16,16,16,-10,-93,16,16,-7,16,-86,16,-13,-16,-87,-88,-75,16,-85,-89,-90,16,-9,-6,-80,16,-14,-84,16,16,16,-77,-78,-8,-82,16,16,-91,-81,-83,-19,16,-76,-92,-17,16,16,-66,-68,-67,-69,-18,-79,-20,-21,]),'STRING':([0,3,4,5,13,14,28,31,36,38,39,40,43,44,52,55,69,77,83,89,93,97,101,126,127,128,129,136,137,138,142,143,163,164,174,185,194,198,200,201,202,204,210,214,216,217,224,234,235,238,239,242,244,254,256,257,259,260,262,263,264,267,268,269,],[17,17,17,17,-11,-12,17,-15,17,17,17,17,17,-10,-93,17,17,-7,17,-86,17,-13,-16,-87,-88,-75,17,-85,-89,-90,17,-9,-6,-80,17,-14,-84,17,17,17,-77,-78,-8,-82,17,17,-91,-81,-83,-19,17,-76,-92,-17,17,17,-66,-68,-67,-69,-18,-79,-20,-21,]),'ID':([0,3,4,5,7,8,10,11,13,14,15,16,17,18,23,27,28,30,31,32,33,35,36,38,39,40,42,43,44,48,49,50,52,54,55,60,62,67,68,69,70,71,72,73,77,82,83,85,86,89,92,93,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,126,127,128,129,131,136,137,138,140,141,142,143,162,163,164,166,167,169,170,174,177,178,180,181,185,187,191,194,198,200,201,202,204,208,209,210,214,216,217,222,223,224,229,230,234,235,238,239,242,244,245,246,247,252,253,254,256,257,259,260,262,263,264,267,268,269,],[8,8,8,8,22,-32,24,25,-11,-12,-29,-30,-31,-33,29,34,35,56,-15,57,-34,-32,35,35,35,35,81,8,-10,57,90,91,-93,94,35,57,57,57,117,35,57,57,122,57,-7,130,8,57,57,-86,139,8,144,-13,57,146,57,-16,57,57,57,57,57,57,57,57,57,57,57,57,-87,-88,-75,8,175,-85,-89,-90,57,57,35,-9,57,-6,-80,57,57,57,196,8,203,203,57,57,-14,57,57,-84,35,8,8,-77,-78,228,228,-8,-82,8,35,203,57,-91,250,251,-81,-83,-19,35,-76,-92,203,203,57,203,203,-17,35,35,-66,-68,-67,-69,-18,-79,-20,-21,]),'VOID':([0,3,4,5,13,14,28,31,36,38,39,40,43,44,52,55,69,77,83,84,89,93,97,101,126,127,128,129,136,137,138,142,143,163,164,174,185,194,198,200,201,202,204,210,214,216,217,224,234,235,238,239,242,244,254,256,257,259,260,262,263,264,267,268,269,],[18,18,18,18,-11,-12,18,-15,18,18,18,18,18,-10,-93,18,18,-7,18,132,-86,18,-13,-16,-87,-88,-75,18,-85,-89,-90,18,-9,-6,-80,18,-14,-84,18,18,18,-77,-78,-8,-82,18,18,-91,-81,-83,-19,18,-76,-92,-17,18,18,-66,-68,-67,-69,-18,-79,-20,-21,]),'LSQUARE':([8,11,15,16,17,18,33,35,42,57,82,118,131,170,203,],[-32,26,-29,-30,-31,-33,-34,71,26,98,26,162,26,26,71,]),'STATIC':([13,14,43,44,],[-11,-12,83,84,]),'EXTENDS':([22,29,],[27,54,]),'LBRACE':([22,28,29,31,34,36,38,39,40,52,55,69,89,94,101,126,127,128,136,137,138,142,164,172,177,178,194,197,198,202,204,214,217,219,222,224,234,235,238,239,240,241,242,244,245,246,252,253,254,256,257,259,260,262,263,264,267,268,269,],[28,36,55,-15,69,36,36,36,36,-93,36,36,-86,142,-16,-87,-88,-75,-85,-89,-90,36,-80,198,36,36,-84,217,36,-77,-78,-82,36,239,36,-91,-81,-83,-19,36,256,257,-76,-92,36,36,36,36,-17,36,36,-66,-68,-67,-69,-18,-79,-20,-21,]),'DOT':([24,35,47,51,56,57,135,203,],[30,72,87,92,96,99,179,72,]),'SEMICOLON':([25,48,56,57,58,59,61,63,64,65,66,74,75,81,88,90,91,93,114,115,120,144,146,148,149,150,151,152,153,154,155,156,157,158,159,160,168,182,183,186,188,189,192,206,212,213,215,225,233,258,],[31,89,97,-55,101,-45,-48,-51,-52,-53,-54,126,127,31,136,137,138,141,-49,-50,164,185,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,194,208,209,-56,-59,-60,214,224,-61,234,235,244,-58,267,]),'EQUAL':([25,81,139,],[32,32,180,]),'RSQUARE':([26,57,59,61,63,64,65,66,114,115,121,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,186,188,189,190,212,233,],[33,-55,-45,-48,-51,-52,-53,-54,-49,-50,165,186,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,-56,-59,-60,212,-61,-58,]),'IF':([28,31,36,38,39,40,52,55,69,89,101,126,127,128,136,137,138,142,164,177,178,194,198,202,204,214,217,222,224,234,235,238,239,242,244,245,246,252,253,254,256,257,259,260,262,263,264,267,268,269,],[45,-15,45,45,45,45,-93,45,45,-86,-16,-87,-88,-75,-85,-89,-90,45,-80,45,45,-84,45,-77,-78,-82,45,45,-91,-81,-83,-19,45,-76,-92,45,45,45,45,-17,45,45,-66,-68,-67,-69,-18,-79,-20,-21,]),'WHILE':([28,31,36,38,39,40,52,55,69,89,101,126,127,128,136,137,138,142,164,177,178,194,198,202,204,214,217,222,224,234,235,238,239,242,244,245,246,252,253,254,256,257,259,260,262,263,264,267,268,269,],[46,-15,46,46,46,46,-93,46,46,-86,-16,-87,-88,-75,-85,-89,-90,46,-80,46,46,-84,46,-77,-78,-82,46,46,-91,-81,-83,-19,46,-76,-92,46,46,46,46,-17,46,46,-66,-68,-67,-69,-18,-79,-20,-21,]),'SYSTEM':([28,31,36,38,39,40,52,55,69,89,101,126,127,128,136,137,138,142,164,177,178,194,198,202,204,214,217,222,224,234,235,238,239,242,244,245,246,252,253,254,256,257,259,260,262,263,264,267,268,269,],[47,-15,47,47,47,47,-93,47,47,-86,-16,-87,-88,-75,-85,-89,-90,47,-80,47,47,-84,47,-77,-78,-82,47,47,-91,-81,-83,-19,47,-76,-92,47,47,47,47,-17,47,47,-66,-68,-67,-69,-18,-79,-20,-21,]),'RETURN':([28,31,36,38,39,40,52,55,69,89,101,126,127,128,136,137,138,142,164,177,178,194,198,202,204,214,217,222,224,234,235,238,239,242,244,245,246,252,253,254,256,257,259,260,262,263,264,267,268,269,],[48,-15,48,48,48,48,-93,48,48,-86,-16,-87,-88,-75,-85,-89,-90,48,-80,48,48,-84,48,-77,-78,-82,48,48,-91,-81,-83,-19,48,-76,-92,48,48,48,48,-17,48,48,-66,-68,-67,-69,-18,-79,-20,-21,]),'PLUS_PLUS':([28,31,35,36,38,39,40,52,55,69,89,101,126,127,128,136,137,138,142,164,177,178,194,198,202,203,204,208,209,214,217,222,224,228,234,235,238,239,242,244,245,246,252,253,254,256,257,259,260,262,263,264,267,268,269,],[49,-15,74,49,49,49,49,-93,49,49,-86,-16,-87,-88,-75,-85,-89,-90,49,-80,49,49,-84,49,-77,74,-78,229,229,-82,49,49,-91,248,-81,-83,-19,49,-76,-92,49,49,49,49,-17,49,49,-66,-68,-67,-69,-18,-79,-20,-21,]),'MINUS_MINUS':([28,31,35,36,38,39,40,52,55,69,89,101,126,127,128,136,137,138,142,164,177,178,194,198,202,203,204,208,209,214,217,222,224,228,234,235,238,239,242,244,245,246,252,253,254,256,257,259,260,262,263,264,267,268,269,],[50,-15,75,50,50,50,50,-93,50,50,-86,-16,-87,-88,-75,-85,-89,-90,50,-80,50,50,-84,50,-77,75,-78,230,230,-82,50,50,-91,249,-81,-83,-19,50,-76,-92,50,50,50,50,-17,50,50,-66,-68,-67,-69,-18,-79,-20,-21,]),'THIS':([28,31,36,38,39,40,52,55,69,89,101,126,127,128,136,137,138,142,164,177,178,194,198,202,204,214,217,222,224,234,235,238,239,242,244,245,246,252,253,254,256,257,259,260,262,263,264,267,268,269,],[51,-15,51,51,51,51,-93,51,51,-86,-16,-87,-88,-75,-85,-89,-90,51,-80,51,51,-84,51,-77,-78,-82,51,51,-91,-81,-83,-19,51,-76,-92,51,51,51,51,-17,51,51,-66,-68,-67,-69,-18,-79,-20,-21,]),'RBRACE':([28,31,36,37,38,39,40,41,52,55,69,76,78,79,80,89,95,101,119,126,127,128,136,137,138,142,164,184,194,198,202,204,214,217,218,224,234,235,237,238,239,242,244,254,255,256,257,259,260,262,263,264,265,266,267,268,269,],[-94,-15,-94,77,-94,-94,-94,-28,-93,-94,-94,128,-25,-26,-27,-86,143,-16,163,-87,-88,-75,-85,-89,-90,-94,-80,210,-84,-94,-77,-78,-82,-94,238,-91,-81,-83,254,-19,-94,-76,-92,-17,264,-94,-94,-66,-68,-67,-69,-18,268,269,-79,-20,-21,]),'FOR':([28,31,36,38,39,40,52,55,69,89,101,126,127,128,136,137,138,142,164,177,178,194,198,202,204,214,217,222,224,234,235,238,239,242,244,245,246,252,253,254,256,257,259,260,262,263,264,267,268,269,],[53,-15,53,53,53,53,-93,53,53,-86,-16,-87,-88,-75,-85,-89,-90,53,-80,53,53,-84,53,-77,-78,-82,53,53,-91,-81,-83,-19,53,-76,-92,53,53,53,53,-17,53,53,-66,-68,-67,-69,-18,-79,-20,-21,]),'MINUS':([31,32,48,57,58,59,60,61,62,63,64,65,66,67,70,71,73,85,86,88,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,120,121,124,133,134,140,141,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,162,166,167,169,180,181,182,183,186,187,188,189,190,191,192,206,212,213,223,233,243,247,261,],[-15,60,60,-55,103,-45,60,-48,60,-51,-52,-53,-54,60,60,60,60,60,60,103,60,60,-16,60,60,60,60,60,60,60,60,60,60,60,60,-49,-50,103,103,103,103,103,103,60,60,103,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,60,60,60,60,60,60,103,103,-56,60,-59,-60,103,60,103,103,-61,103,60,-58,103,60,103,]),'NOT':([31,32,48,60,62,67,70,71,73,85,86,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,140,141,162,166,167,169,180,181,187,191,223,247,],[-15,62,62,62,62,62,62,62,62,62,62,62,62,-16,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'INT_LITERAL':([31,32,48,60,62,67,70,71,73,85,86,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,140,141,162,166,167,169,180,181,187,191,223,247,],[-15,63,63,63,63,63,63,63,63,63,63,63,63,-16,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'TRUE':([31,32,48,60,62,67,70,71,73,85,86,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,140,141,162,166,167,169,180,181,187,191,223,247,],[-15,64,64,64,64,64,64,64,64,64,64,64,64,-16,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'FALSE':([31,32,48,60,62,67,70,71,73,85,86,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,140,141,162,166,167,169,180,181,187,191,223,247,],[-15,65,65,65,65,65,65,65,65,65,65,65,65,-16,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'STRING_LITERAL':([31,32,48,60,62,67,70,71,73,85,86,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,140,141,162,166,167,169,180,181,187,191,223,247,],[-15,66,66,66,66,66,66,66,66,66,66,66,66,-16,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'NEW':([31,32,48,60,62,67,70,71,73,85,86,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,140,141,162,166,167,169,180,181,187,191,223,247,],[-15,68,68,68,68,68,68,68,68,68,68,68,68,-16,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'LPAREN':([31,32,35,45,46,48,53,57,60,62,67,70,71,73,81,85,86,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,117,122,130,139,140,141,146,162,166,167,169,175,176,180,181,187,191,203,205,223,247,],[-15,67,73,85,86,67,93,100,67,67,67,67,67,67,129,67,67,67,67,-16,67,67,67,67,67,67,67,67,67,67,67,67,161,167,174,181,67,67,187,67,67,67,67,200,201,67,67,67,67,73,223,67,67,]),'EQUALS':([35,57,58,59,61,63,64,65,66,88,114,115,116,120,121,122,124,133,134,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,165,182,183,186,188,189,190,192,203,206,212,213,228,233,243,261,],[70,-55,106,-45,-48,-51,-52,-53,-54,106,-49,-50,106,106,106,166,106,106,106,106,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,191,106,106,-56,-59,-60,106,106,70,106,-61,106,247,-58,106,106,]),'ELSE':([52,89,126,127,128,136,137,138,164,194,202,204,214,224,234,235,242,244,259,260,262,263,267,],[-93,-86,-87,-88,-75,-85,-89,-90,-80,-84,222,-78,-82,-91,-81,-83,-76,-92,-66,-68,-67,-69,-79,]),'TIMES':([57,59,61,63,64,65,66,114,115,146,148,149,150,151,152,153,154,155,156,157,158,159,160,186,188,189,212,233,],[-55,112,-48,-51,-52,-53,-54,-49,-50,-57,112,112,112,112,112,112,112,112,112,112,-46,-47,-62,-56,-59,-60,-61,-58,]),'DIVIDE':([57,59,61,63,64,65,66,114,115,146,148,149,150,151,152,153,154,155,156,157,158,159,160,186,188,189,212,233,],[-55,113,-48,-51,-52,-53,-54,-49,-50,-57,113,113,113,113,113,113,113,113,113,113,-46,-47,-62,-56,-59,-60,-61,-58,]),'PLUS':([57,58,59,61,63,64,65,66,88,114,115,116,120,121,124,133,134,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,182,183,186,188,189,190,192,206,212,213,233,243,261,],[-55,102,-45,-48,-51,-52,-53,-54,102,-49,-50,102,102,102,102,102,102,102,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,102,102,-56,-59,-60,102,102,102,-61,102,-58,102,102,]),'AND':([57,58,59,61,63,64,65,66,88,114,115,116,120,121,124,133,134,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,182,183,186,188,189,190,192,206,212,213,233,243,261,],[-55,104,-45,-48,-51,-52,-53,-54,104,-49,-50,104,104,104,104,104,104,104,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,104,104,-56,-59,-60,104,104,104,-61,104,-58,104,104,]),'OR':([57,58,59,61,63,64,65,66,88,114,115,116,120,121,124,133,134,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,182,183,186,188,189,190,192,206,212,213,233,243,261,],[-55,105,-45,-48,-51,-52,-53,-54,105,-49,-50,105,105,105,105,105,105,105,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,105,105,-56,-59,-60,105,105,105,-61,105,-58,105,105,]),'NOT_EQUALS':([57,58,59,61,63,64,65,66,88,114,115,116,120,121,124,133,134,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,182,183,186,188,189,190,192,206,212,213,233,243,261,],[-55,107,-45,-48,-51,-52,-53,-54,107,-49,-50,107,107,107,107,107,107,107,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,107,107,-56,-59,-60,107,107,107,-61,107,-58,107,107,]),'LESS_THAN':([57,58,59,61,63,64,65,66,88,114,115,116,120,121,124,133,134,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,182,183,186,188,189,190,192,206,212,213,233,243,261,],[-55,108,-45,-48,-51,-52,-53,-54,108,-49,-50,108,108,108,108,108,108,108,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,108,108,-56,-59,-60,108,108,108,-61,108,-58,108,108,]),'LESS_THAN_OR_EQUAL':([57,58,59,61,63,64,65,66,88,114,115,116,120,121,124,133,134,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,182,183,186,188,189,190,192,206,212,213,233,243,261,],[-55,109,-45,-48,-51,-52,-53,-54,109,-49,-50,109,109,109,109,109,109,109,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,109,109,-56,-59,-60,109,109,109,-61,109,-58,109,109,]),'GREATER_THAN':([57,58,59,61,63,64,65,66,88,114,115,116,120,121,124,133,134,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,182,183,186,188,189,190,192,206,212,213,233,243,261,],[-55,110,-45,-48,-51,-52,-53,-54,110,-49,-50,110,110,110,110,110,110,110,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,110,110,-56,-59,-60,110,110,110,-61,110,-58,110,110,]),'GREATER_THAN_OR_EQUAL':([57,58,59,61,63,64,65,66,88,114,115,116,120,121,124,133,134,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,182,183,186,188,189,190,192,206,212,213,233,243,261,],[-55,111,-45,-48,-51,-52,-53,-54,111,-49,-50,111,111,111,111,111,111,111,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,111,111,-56,-59,-60,111,111,111,-61,111,-58,111,111,]),'RPAREN':([57,59,61,63,64,65,66,73,100,114,115,116,123,124,125,129,133,134,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,167,169,171,173,174,181,186,187,188,189,193,195,196,199,200,201,207,211,212,216,220,221,226,227,231,232,233,236,243,248,249,250,251,261,],[-55,-45,-48,-51,-52,-53,-54,-94,-94,-49,-50,160,168,-63,-65,172,177,178,-57,188,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,189,-94,-94,197,-24,-94,-94,-56,-94,-59,-60,215,-64,-22,219,-94,-94,225,233,-61,-94,240,241,245,246,252,253,-58,-23,258,-71,-72,-73,-74,-70,]),'COMMA':([57,59,61,63,64,65,66,114,115,124,146,148,149,150,151,152,153,154,155,156,157,158,159,160,186,188,189,196,212,233,],[-55,-45,-48,-51,-52,-53,-54,-49,-50,169,-57,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-47,-62,-56,-59,-60,216,-61,-58,]),'OUT':([87,],[135,]),'MAIN':([132,],[176,]),'PRINTLN':([179,],[205,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'body_program':([0,3,4,5,],[2,19,20,21,]),'class_decl':([0,3,4,5,],[3,3,3,3,]),'import_decl':([0,3,4,5,],[4,4,4,4,]),'var_decl':([0,3,4,5,28,36,38,39,40,55,69,93,142,198,217,239,256,257,],[5,5,5,5,38,38,38,38,38,38,38,140,38,38,38,38,38,38,]),'empty':([0,3,4,5,28,36,38,39,40,55,69,73,100,129,142,167,169,174,181,187,198,200,201,216,217,239,256,257,],[6,6,6,6,41,41,41,41,41,41,41,125,125,173,41,125,125,173,125,125,41,173,173,173,41,41,41,41,]),'access_modifier':([0,3,4,5,28,36,38,39,40,55,69,142,198,217,239,256,257,],[9,9,9,9,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'type':([0,3,4,5,28,36,38,39,40,43,55,69,83,93,129,142,174,198,200,201,216,217,239,256,257,],[11,11,11,11,42,42,42,42,42,82,42,42,131,11,170,42,170,42,170,170,170,42,42,42,42,]),'body':([28,36,38,39,40,55,69,142,198,217,239,256,257,],[37,76,78,79,80,95,119,184,218,237,255,265,266,]),'method_decl':([28,36,38,39,40,55,69,142,198,217,239,256,257,],[39,39,39,39,39,39,39,39,39,39,39,39,39,]),'statement':([28,36,38,39,40,55,69,142,177,178,198,217,222,239,245,246,252,253,256,257,],[40,40,40,40,40,40,40,40,202,204,40,40,242,40,259,260,262,263,40,40,]),'for_loop':([28,36,38,39,40,55,69,142,177,178,198,217,222,239,245,246,252,253,256,257,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'expr':([32,48,67,70,71,73,85,86,98,100,140,141,162,166,167,169,180,181,187,191,223,247,],[58,88,116,120,121,124,133,134,145,124,182,183,190,192,124,124,206,124,124,213,243,261,]),'term':([32,48,67,70,71,73,85,86,98,100,102,103,104,105,106,107,108,109,110,111,140,141,162,166,167,169,180,181,187,191,223,247,],[59,59,59,59,59,59,59,59,59,59,148,149,150,151,152,153,154,155,156,157,59,59,59,59,59,59,59,59,59,59,59,59,]),'factor':([32,48,60,62,67,70,71,73,85,86,98,100,102,103,104,105,106,107,108,109,110,111,112,113,140,141,162,166,167,169,180,181,187,191,223,247,],[61,61,114,115,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,158,159,61,61,61,61,61,61,61,61,61,61,61,61,]),'args':([73,100,167,169,181,187,],[123,147,193,195,207,211,]),'params':([129,174,200,201,216,],[171,199,220,221,236,]),'assign_expr':([208,209,],[226,231,]),'increment_expr':([208,209,],[227,232,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> body_program','program',1,'p_program','Parser.py',23),
  ('body_program -> class_decl body_program','body_program',2,'p_body_program','Parser.py',28),
  ('body_program -> import_decl body_program','body_program',2,'p_body_program','Parser.py',29),
  ('body_program -> var_decl body_program','body_program',2,'p_body_program','Parser.py',30),
  ('body_program -> empty','body_program',1,'p_body_program','Parser.py',31),
  ('class_decl -> CLASS ID EXTENDS ID LBRACE body RBRACE','class_decl',7,'p_class_decl','Parser.py',37),
  ('class_decl -> CLASS ID LBRACE body RBRACE','class_decl',5,'p_class_decl','Parser.py',38),
  ('class_decl -> access_modifier CLASS ID EXTENDS ID LBRACE body RBRACE','class_decl',8,'p_class_decl','Parser.py',39),
  ('class_decl -> access_modifier CLASS ID LBRACE body RBRACE','class_decl',6,'p_class_decl','Parser.py',40),
  ('access_modifier -> PUBLIC','access_modifier',1,'p_access_modifier','Parser.py',46),
  ('access_modifier -> PRIVATE','access_modifier',1,'p_access_modifier','Parser.py',47),
  ('access_modifier -> PROTECTED','access_modifier',1,'p_access_modifier','Parser.py',48),
  ('import_decl -> IMPORT ID DOT ID SEMICOLON','import_decl',5,'p_import_decl','Parser.py',54),
  ('import_decl -> IMPORT ID DOT ID DOT ID SEMICOLON','import_decl',7,'p_import_decl','Parser.py',55),
  ('var_decl -> type ID SEMICOLON','var_decl',3,'p_var_decl','Parser.py',61),
  ('var_decl -> type ID EQUAL expr SEMICOLON','var_decl',5,'p_var_decl','Parser.py',62),
  ('method_decl -> type ID LPAREN params RPAREN LBRACE body RBRACE','method_decl',8,'p_method_decl','Parser.py',68),
  ('method_decl -> access_modifier type ID LPAREN params RPAREN LBRACE body RBRACE','method_decl',9,'p_method_decl','Parser.py',69),
  ('method_decl -> type ID LPAREN RPAREN LBRACE body RBRACE','method_decl',7,'p_method_decl','Parser.py',70),
  ('method_decl -> access_modifier STATIC type ID LPAREN params RPAREN LBRACE body RBRACE','method_decl',10,'p_method_decl','Parser.py',71),
  ('method_decl -> PUBLIC STATIC VOID MAIN LPAREN params RPAREN LBRACE body RBRACE','method_decl',10,'p_method_decl','Parser.py',72),
  ('params -> type ID','params',2,'p_params','Parser.py',78),
  ('params -> type ID COMMA params','params',4,'p_params','Parser.py',79),
  ('params -> empty','params',1,'p_params','Parser.py',80),
  ('body -> var_decl body','body',2,'p_body','Parser.py',86),
  ('body -> method_decl body','body',2,'p_body','Parser.py',87),
  ('body -> statement body','body',2,'p_body','Parser.py',88),
  ('body -> empty','body',1,'p_body','Parser.py',89),
  ('type -> INT','type',1,'p_type','Parser.py',95),
  ('type -> BOOLEAN','type',1,'p_type','Parser.py',96),
  ('type -> STRING','type',1,'p_type','Parser.py',97),
  ('type -> ID','type',1,'p_type','Parser.py',98),
  ('type -> VOID','type',1,'p_type','Parser.py',99),
  ('type -> type LSQUARE RSQUARE','type',3,'p_type','Parser.py',100),
  ('expr -> expr PLUS term','expr',3,'p_expr','Parser.py',106),
  ('expr -> expr MINUS term','expr',3,'p_expr','Parser.py',107),
  ('expr -> expr AND term','expr',3,'p_expr','Parser.py',108),
  ('expr -> expr OR term','expr',3,'p_expr','Parser.py',109),
  ('expr -> expr EQUALS term','expr',3,'p_expr','Parser.py',110),
  ('expr -> expr NOT_EQUALS term','expr',3,'p_expr','Parser.py',111),
  ('expr -> expr LESS_THAN term','expr',3,'p_expr','Parser.py',112),
  ('expr -> expr LESS_THAN_OR_EQUAL term','expr',3,'p_expr','Parser.py',113),
  ('expr -> expr GREATER_THAN term','expr',3,'p_expr','Parser.py',114),
  ('expr -> expr GREATER_THAN_OR_EQUAL term','expr',3,'p_expr','Parser.py',115),
  ('expr -> term','expr',1,'p_expr','Parser.py',116),
  ('term -> term TIMES factor','term',3,'p_term','Parser.py',122),
  ('term -> term DIVIDE factor','term',3,'p_term','Parser.py',123),
  ('term -> factor','term',1,'p_term','Parser.py',124),
  ('factor -> MINUS factor','factor',2,'p_factor','Parser.py',130),
  ('factor -> NOT factor','factor',2,'p_factor','Parser.py',131),
  ('factor -> INT_LITERAL','factor',1,'p_factor','Parser.py',132),
  ('factor -> TRUE','factor',1,'p_factor','Parser.py',133),
  ('factor -> FALSE','factor',1,'p_factor','Parser.py',134),
  ('factor -> STRING_LITERAL','factor',1,'p_factor','Parser.py',135),
  ('factor -> ID','factor',1,'p_factor','Parser.py',136),
  ('factor -> ID LSQUARE expr RSQUARE','factor',4,'p_factor','Parser.py',137),
  ('factor -> ID DOT ID','factor',3,'p_factor','Parser.py',138),
  ('factor -> ID DOT ID LPAREN args RPAREN','factor',6,'p_factor','Parser.py',139),
  ('factor -> ID LPAREN args RPAREN','factor',4,'p_factor','Parser.py',140),
  ('factor -> NEW ID LPAREN RPAREN','factor',4,'p_factor','Parser.py',141),
  ('factor -> NEW INT LSQUARE expr RSQUARE','factor',5,'p_factor','Parser.py',142),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor','Parser.py',143),
  ('args -> expr','args',1,'p_args','Parser.py',149),
  ('args -> expr COMMA args','args',3,'p_args','Parser.py',150),
  ('args -> empty','args',1,'p_args','Parser.py',151),
  ('for_loop -> FOR LPAREN var_decl expr SEMICOLON assign_expr RPAREN statement','for_loop',8,'p_for_loop','Parser.py',157),
  ('for_loop -> FOR LPAREN SEMICOLON expr SEMICOLON assign_expr RPAREN statement','for_loop',8,'p_for_loop','Parser.py',158),
  ('for_loop -> FOR LPAREN var_decl expr SEMICOLON increment_expr RPAREN statement','for_loop',8,'p_for_loop','Parser.py',159),
  ('for_loop -> FOR LPAREN SEMICOLON expr SEMICOLON increment_expr RPAREN statement','for_loop',8,'p_for_loop','Parser.py',160),
  ('assign_expr -> ID EQUALS expr','assign_expr',3,'p_assign_expr','Parser.py',165),
  ('increment_expr -> ID PLUS_PLUS','increment_expr',2,'p_increment_expr','Parser.py',170),
  ('increment_expr -> ID MINUS_MINUS','increment_expr',2,'p_increment_expr','Parser.py',171),
  ('increment_expr -> PLUS_PLUS ID','increment_expr',2,'p_increment_expr','Parser.py',172),
  ('increment_expr -> MINUS_MINUS ID','increment_expr',2,'p_increment_expr','Parser.py',173),
  ('statement -> LBRACE body RBRACE','statement',3,'p_statement','Parser.py',179),
  ('statement -> IF LPAREN expr RPAREN statement ELSE statement','statement',7,'p_statement','Parser.py',180),
  ('statement -> IF LPAREN expr RPAREN statement','statement',5,'p_statement','Parser.py',181),
  ('statement -> WHILE LPAREN expr RPAREN statement','statement',5,'p_statement','Parser.py',182),
  ('statement -> SYSTEM DOT OUT DOT PRINTLN LPAREN expr RPAREN SEMICOLON','statement',9,'p_statement','Parser.py',183),
  ('statement -> ID EQUALS expr SEMICOLON','statement',4,'p_statement','Parser.py',184),
  ('statement -> ID LSQUARE expr RSQUARE EQUALS expr SEMICOLON','statement',7,'p_statement','Parser.py',185),
  ('statement -> ID DOT ID EQUALS expr SEMICOLON','statement',6,'p_statement','Parser.py',186),
  ('statement -> ID DOT ID LPAREN args RPAREN SEMICOLON','statement',7,'p_statement','Parser.py',187),
  ('statement -> ID LPAREN args RPAREN SEMICOLON','statement',5,'p_statement','Parser.py',188),
  ('statement -> RETURN expr SEMICOLON','statement',3,'p_statement','Parser.py',189),
  ('statement -> RETURN SEMICOLON','statement',2,'p_statement','Parser.py',190),
  ('statement -> ID PLUS_PLUS SEMICOLON','statement',3,'p_statement','Parser.py',191),
  ('statement -> ID MINUS_MINUS SEMICOLON','statement',3,'p_statement','Parser.py',192),
  ('statement -> PLUS_PLUS ID SEMICOLON','statement',3,'p_statement','Parser.py',193),
  ('statement -> MINUS_MINUS ID SEMICOLON','statement',3,'p_statement','Parser.py',194),
  ('statement -> THIS DOT ID EQUAL expr SEMICOLON','statement',6,'p_statement','Parser.py',195),
  ('statement -> THIS DOT ID LPAREN args RPAREN SEMICOLON','statement',7,'p_statement','Parser.py',196),
  ('statement -> for_loop','statement',1,'p_statement','Parser.py',197),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',202),
]
