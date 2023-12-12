# Generated from C:/Users/Main user/Desktop/compiler_design_fall_2023/HW2/gen/main.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mainParser import mainParser
else:
    from mainParser import mainParser

# This class defines a complete listener for a parse tree produced by mainParser.
class mainListener(ParseTreeListener):

    # Enter a parse tree produced by mainParser#equation.
    def enterEquation(self, ctx:mainParser.EquationContext):
        pass

    # Exit a parse tree produced by mainParser#equation.
    def exitEquation(self, ctx:mainParser.EquationContext):
        pass


    # Enter a parse tree produced by mainParser#expression.
    def enterExpression(self, ctx:mainParser.ExpressionContext):
        pass

    # Exit a parse tree produced by mainParser#expression.
    def exitExpression(self, ctx:mainParser.ExpressionContext):
        pass


    # Enter a parse tree produced by mainParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:mainParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by mainParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:mainParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by mainParser#powExpression.
    def enterPowExpression(self, ctx:mainParser.PowExpressionContext):
        pass

    # Exit a parse tree produced by mainParser#powExpression.
    def exitPowExpression(self, ctx:mainParser.PowExpressionContext):
        pass


    # Enter a parse tree produced by mainParser#signedAtom.
    def enterSignedAtom(self, ctx:mainParser.SignedAtomContext):
        pass

    # Exit a parse tree produced by mainParser#signedAtom.
    def exitSignedAtom(self, ctx:mainParser.SignedAtomContext):
        pass


    # Enter a parse tree produced by mainParser#atom.
    def enterAtom(self, ctx:mainParser.AtomContext):
        pass

    # Exit a parse tree produced by mainParser#atom.
    def exitAtom(self, ctx:mainParser.AtomContext):
        pass


    # Enter a parse tree produced by mainParser#scientific.
    def enterScientific(self, ctx:mainParser.ScientificContext):
        pass

    # Exit a parse tree produced by mainParser#scientific.
    def exitScientific(self, ctx:mainParser.ScientificContext):
        pass


    # Enter a parse tree produced by mainParser#constant.
    def enterConstant(self, ctx:mainParser.ConstantContext):
        pass

    # Exit a parse tree produced by mainParser#constant.
    def exitConstant(self, ctx:mainParser.ConstantContext):
        pass


    # Enter a parse tree produced by mainParser#variable.
    def enterVariable(self, ctx:mainParser.VariableContext):
        pass

    # Exit a parse tree produced by mainParser#variable.
    def exitVariable(self, ctx:mainParser.VariableContext):
        pass


    # Enter a parse tree produced by mainParser#func_.
    def enterFunc_(self, ctx:mainParser.Func_Context):
        pass

    # Exit a parse tree produced by mainParser#func_.
    def exitFunc_(self, ctx:mainParser.Func_Context):
        pass


    # Enter a parse tree produced by mainParser#funcname.
    def enterFuncname(self, ctx:mainParser.FuncnameContext):
        pass

    # Exit a parse tree produced by mainParser#funcname.
    def exitFuncname(self, ctx:mainParser.FuncnameContext):
        pass


    # Enter a parse tree produced by mainParser#relop.
    def enterRelop(self, ctx:mainParser.RelopContext):
        pass

    # Exit a parse tree produced by mainParser#relop.
    def exitRelop(self, ctx:mainParser.RelopContext):
        pass



del mainParser