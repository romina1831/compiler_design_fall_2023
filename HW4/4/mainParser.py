# Generated from C:/Users/Main user/Desktop/compiler_design_fall_2023/HW35/gen/main.g4 by ANTLR 1.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,2,1,2,1,2,5,2,41,8,2,
        10,2,12,2,44,9,2,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,60,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,69,8,
        5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,9,82,8,9,10,9,12,
        9,85,9,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,
        14,16,18,20,22,0,5,1,0,12,13,1,0,14,15,1,0,22,24,1,0,1,9,1,0,16,
        18,90,0,24,1,0,0,0,2,29,1,0,0,0,4,37,1,0,0,0,6,45,1,0,0,0,8,59,1,
        0,0,0,10,68,1,0,0,0,12,70,1,0,0,0,14,72,1,0,0,0,16,74,1,0,0,0,18,
        76,1,0,0,0,20,88,1,0,0,0,22,90,1,0,0,0,24,25,3,2,1,0,25,26,3,22,
        11,0,26,27,3,2,1,0,27,28,5,0,0,1,28,1,1,0,0,0,29,34,3,4,2,0,30,31,
        7,0,0,0,31,33,3,4,2,0,32,30,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,
        34,35,1,0,0,0,35,3,1,0,0,0,36,34,1,0,0,0,37,42,3,6,3,0,38,39,7,1,
        0,0,39,41,3,6,3,0,40,38,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,
        1,0,0,0,43,5,1,0,0,0,44,42,1,0,0,0,45,50,3,8,4,0,46,47,5,21,0,0,
        47,49,3,8,4,0,48,46,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,
        0,0,0,51,7,1,0,0,0,52,50,1,0,0,0,53,54,5,12,0,0,54,60,3,8,4,0,55,
        56,5,13,0,0,56,60,3,8,4,0,57,60,3,18,9,0,58,60,3,10,5,0,59,53,1,
        0,0,0,59,55,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,9,1,0,0,0,61,
        69,3,12,6,0,62,69,3,16,8,0,63,69,3,14,7,0,64,65,5,10,0,0,65,66,3,
        2,1,0,66,67,5,11,0,0,67,69,1,0,0,0,68,61,1,0,0,0,68,62,1,0,0,0,68,
        63,1,0,0,0,68,64,1,0,0,0,69,11,1,0,0,0,70,71,5,26,0,0,71,13,1,0,
        0,0,72,73,7,2,0,0,73,15,1,0,0,0,74,75,5,25,0,0,75,17,1,0,0,0,76,
        77,3,20,10,0,77,78,5,10,0,0,78,83,3,2,1,0,79,80,5,19,0,0,80,82,3,
        2,1,0,81,79,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,
        86,1,0,0,0,85,83,1,0,0,0,86,87,5,11,0,0,87,19,1,0,0,0,88,89,7,3,
        0,0,89,21,1,0,0,0,90,91,7,4,0,0,91,23,1,0,0,0,6,34,42,50,59,68,83
    ]

class mainParser ( Parser ):

    grammarFileName = "main.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'cos'", "'sin'", "'tan'", "'acos'", "'asin'", 
                     "'atan'", "'ln'", "'log'", "'sqrt'", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'='", "','", 
                     "'.'", "'^'", "'pi'", "<INVALID>", "'i'" ]

    symbolicNames = [ "<INVALID>", "COS", "SIN", "TAN", "ACOS", "ASIN", 
                      "ATAN", "LN", "LOG", "SQRT", "LPAREN", "RPAREN", "PLUS", 
                      "MINUS", "TIMES", "DIV", "GT", "LT", "EQ", "COMMA", 
                      "POINT", "POW", "PI", "EULER", "I", "VARIABLE", "SCIENTIFIC_NUMBER", 
                      "WS" ]

    RULE_equation = 0
    RULE_expression = 1
    RULE_multiplyingExpression = 2
    RULE_powExpression = 3
    RULE_signedAtom = 4
    RULE_atom = 5
    RULE_scientific = 6
    RULE_constant = 7
    RULE_variable = 8
    RULE_func_ = 9
    RULE_funcname = 10
    RULE_relop = 11

    ruleNames =  [ "equation", "expression", "multiplyingExpression", "powExpression", 
                   "signedAtom", "atom", "scientific", "constant", "variable", 
                   "func_", "funcname", "relop" ]

    EOF = Token.EOF
    COS=1
    SIN=2
    TAN=3
    ACOS=4
    ASIN=5
    ATAN=6
    LN=7
    LOG=8
    SQRT=9
    LPAREN=10
    RPAREN=11
    PLUS=12
    MINUS=13
    TIMES=14
    DIV=15
    GT=16
    LT=17
    EQ=18
    COMMA=19
    POINT=20
    POW=21
    PI=22
    EULER=23
    I=24
    VARIABLE=25
    SCIENTIFIC_NUMBER=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("1.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(mainParser.ExpressionContext,i)


        def relop(self):
            return self.getTypedRuleContext(mainParser.RelopContext,0)


        def EOF(self):
            return self.getToken(mainParser.EOF, 0)

        def getRuleIndex(self):
            return mainParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquation" ):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)




    def equation(self):

        localctx = mainParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.expression()
            self.state = 25
            self.relop()
            self.state = 26
            self.expression()
            self.state = 27
            self.match(mainParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplyingExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.MultiplyingExpressionContext)
            else:
                return self.getTypedRuleContext(mainParser.MultiplyingExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.PLUS)
            else:
                return self.getToken(mainParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.MINUS)
            else:
                return self.getToken(mainParser.MINUS, i)

        def getRuleIndex(self):
            return mainParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = mainParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.multiplyingExpression()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==13:
                self.state = 30
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 31
                self.multiplyingExpression()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def powExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.PowExpressionContext)
            else:
                return self.getTypedRuleContext(mainParser.PowExpressionContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.TIMES)
            else:
                return self.getToken(mainParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.DIV)
            else:
                return self.getToken(mainParser.DIV, i)

        def getRuleIndex(self):
            return mainParser.RULE_multiplyingExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyingExpression" ):
                listener.enterMultiplyingExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyingExpression" ):
                listener.exitMultiplyingExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplyingExpression" ):
                return visitor.visitMultiplyingExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplyingExpression(self):

        localctx = mainParser.MultiplyingExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_multiplyingExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.powExpression()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==15:
                self.state = 38
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 39
                self.powExpression()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signedAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.SignedAtomContext)
            else:
                return self.getTypedRuleContext(mainParser.SignedAtomContext,i)


        def POW(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.POW)
            else:
                return self.getToken(mainParser.POW, i)

        def getRuleIndex(self):
            return mainParser.RULE_powExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowExpression" ):
                listener.enterPowExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowExpression" ):
                listener.exitPowExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowExpression" ):
                return visitor.visitPowExpression(self)
            else:
                return visitor.visitChildren(self)




    def powExpression(self):

        localctx = mainParser.PowExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_powExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.signedAtom()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 46
                self.match(mainParser.POW)
                self.state = 47
                self.signedAtom()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(mainParser.PLUS, 0)

        def signedAtom(self):
            return self.getTypedRuleContext(mainParser.SignedAtomContext,0)


        def MINUS(self):
            return self.getToken(mainParser.MINUS, 0)

        def func_(self):
            return self.getTypedRuleContext(mainParser.Func_Context,0)


        def atom(self):
            return self.getTypedRuleContext(mainParser.AtomContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_signedAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedAtom" ):
                listener.enterSignedAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedAtom" ):
                listener.exitSignedAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignedAtom" ):
                return visitor.visitSignedAtom(self)
            else:
                return visitor.visitChildren(self)




    def signedAtom(self):

        localctx = mainParser.SignedAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_signedAtom)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(mainParser.PLUS)
                self.state = 54
                self.signedAtom()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(mainParser.MINUS)
                self.state = 56
                self.signedAtom()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.func_()
                pass
            elif token in [10, 22, 23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scientific(self):
            return self.getTypedRuleContext(mainParser.ScientificContext,0)


        def variable(self):
            return self.getTypedRuleContext(mainParser.VariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(mainParser.ConstantContext,0)


        def LPAREN(self):
            return self.getToken(mainParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(mainParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(mainParser.RPAREN, 0)

        def getRuleIndex(self):
            return mainParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = mainParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.scientific()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.variable()
                pass
            elif token in [22, 23, 24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.constant()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.match(mainParser.LPAREN)
                self.state = 65
                self.expression()
                self.state = 66
                self.match(mainParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScientificContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCIENTIFIC_NUMBER(self):
            return self.getToken(mainParser.SCIENTIFIC_NUMBER, 0)

        def getRuleIndex(self):
            return mainParser.RULE_scientific

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScientific" ):
                listener.enterScientific(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScientific" ):
                listener.exitScientific(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScientific" ):
                return visitor.visitScientific(self)
            else:
                return visitor.visitChildren(self)




    def scientific(self):

        localctx = mainParser.ScientificContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_scientific)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(mainParser.SCIENTIFIC_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PI(self):
            return self.getToken(mainParser.PI, 0)

        def EULER(self):
            return self.getToken(mainParser.EULER, 0)

        def I(self):
            return self.getToken(mainParser.I, 0)

        def getRuleIndex(self):
            return mainParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = mainParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(mainParser.VARIABLE, 0)

        def getRuleIndex(self):
            return mainParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = mainParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(mainParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcname(self):
            return self.getTypedRuleContext(mainParser.FuncnameContext,0)


        def LPAREN(self):
            return self.getToken(mainParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(mainParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(mainParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.COMMA)
            else:
                return self.getToken(mainParser.COMMA, i)

        def getRuleIndex(self):
            return mainParser.RULE_func_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_" ):
                listener.enterFunc_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_" ):
                listener.exitFunc_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_" ):
                return visitor.visitFunc_(self)
            else:
                return visitor.visitChildren(self)




    def func_(self):

        localctx = mainParser.Func_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.funcname()
            self.state = 77
            self.match(mainParser.LPAREN)
            self.state = 78
            self.expression()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 79
                self.match(mainParser.COMMA)
                self.state = 80
                self.expression()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(mainParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COS(self):
            return self.getToken(mainParser.COS, 0)

        def TAN(self):
            return self.getToken(mainParser.TAN, 0)

        def SIN(self):
            return self.getToken(mainParser.SIN, 0)

        def ACOS(self):
            return self.getToken(mainParser.ACOS, 0)

        def ATAN(self):
            return self.getToken(mainParser.ATAN, 0)

        def ASIN(self):
            return self.getToken(mainParser.ASIN, 0)

        def LOG(self):
            return self.getToken(mainParser.LOG, 0)

        def LN(self):
            return self.getToken(mainParser.LN, 0)

        def SQRT(self):
            return self.getToken(mainParser.SQRT, 0)

        def getRuleIndex(self):
            return mainParser.RULE_funcname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncname" ):
                listener.enterFuncname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncname" ):
                listener.exitFuncname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncname" ):
                return visitor.visitFuncname(self)
            else:
                return visitor.visitChildren(self)




    def funcname(self):

        localctx = mainParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1022) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(mainParser.EQ, 0)

        def GT(self):
            return self.getToken(mainParser.GT, 0)

        def LT(self):
            return self.getToken(mainParser.LT, 0)

        def getRuleIndex(self):
            return mainParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = mainParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





