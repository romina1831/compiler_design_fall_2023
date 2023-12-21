# Generated from C:/Users/Main user/Desktop/compiler_design_fall_2023/HW2/gen/main.g4 by ANTLR 1.13.1
from antlr4 import *
if "." in __name__:
    from .mainParser import mainParser
else:
    from mainParser import mainParser

# This class defines a complete generic visitor for a parse tree produced by mainParser.

class mainVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mainParser#equation.
    def visitEquation(self, ctx:mainParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#expression.
    def visitExpression(self, ctx:mainParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#multiplyingExpression.
    def visitMultiplyingExpression(self, ctx:mainParser.MultiplyingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#powExpression.
    def visitPowExpression(self, ctx:mainParser.PowExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#signedAtom.
    def visitSignedAtom(self, ctx:mainParser.SignedAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#atom.
    def visitAtom(self, ctx:mainParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#scientific.
    def visitScientific(self, ctx:mainParser.ScientificContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#constant.
    def visitConstant(self, ctx:mainParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#variable.
    def visitVariable(self, ctx:mainParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#func_.
    def visitFunc_(self, ctx:mainParser.Func_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#funcname.
    def visitFuncname(self, ctx:mainParser.FuncnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#relop.
    def visitRelop(self, ctx:mainParser.RelopContext):
        return self.visitChildren(ctx)



del mainParser