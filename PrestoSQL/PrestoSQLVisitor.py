# Generated from PrestoSQL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrestoSQLParser import PrestoSQLParser
else:
    from PrestoSQLParser import PrestoSQLParser

# This class defines a complete generic visitor for a parse tree produced by PrestoSQLParser.

class PrestoSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrestoSQLParser#singleStatement.
    def visitSingleStatement(self, ctx:PrestoSQLParser.SingleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#standaloneExpression.
    def visitStandaloneExpression(self, ctx:PrestoSQLParser.StandaloneExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#standaloneRoutineBody.
    def visitStandaloneRoutineBody(self, ctx:PrestoSQLParser.StandaloneRoutineBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#statementDefault.
    def visitStatementDefault(self, ctx:PrestoSQLParser.StatementDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#use.
    def visitUse(self, ctx:PrestoSQLParser.UseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#createSchema.
    def visitCreateSchema(self, ctx:PrestoSQLParser.CreateSchemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#dropSchema.
    def visitDropSchema(self, ctx:PrestoSQLParser.DropSchemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#renameSchema.
    def visitRenameSchema(self, ctx:PrestoSQLParser.RenameSchemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#createTableAsSelect.
    def visitCreateTableAsSelect(self, ctx:PrestoSQLParser.CreateTableAsSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#createTable.
    def visitCreateTable(self, ctx:PrestoSQLParser.CreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#dropTable.
    def visitDropTable(self, ctx:PrestoSQLParser.DropTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#insertInto.
    def visitInsertInto(self, ctx:PrestoSQLParser.InsertIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#delete.
    def visitDelete(self, ctx:PrestoSQLParser.DeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#renameTable.
    def visitRenameTable(self, ctx:PrestoSQLParser.RenameTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#renameColumn.
    def visitRenameColumn(self, ctx:PrestoSQLParser.RenameColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#dropColumn.
    def visitDropColumn(self, ctx:PrestoSQLParser.DropColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#addColumn.
    def visitAddColumn(self, ctx:PrestoSQLParser.AddColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#analyze.
    def visitAnalyze(self, ctx:PrestoSQLParser.AnalyzeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#createView.
    def visitCreateView(self, ctx:PrestoSQLParser.CreateViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#dropView.
    def visitDropView(self, ctx:PrestoSQLParser.DropViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#createFunction.
    def visitCreateFunction(self, ctx:PrestoSQLParser.CreateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#alterFunction.
    def visitAlterFunction(self, ctx:PrestoSQLParser.AlterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#dropFunction.
    def visitDropFunction(self, ctx:PrestoSQLParser.DropFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#call.
    def visitCall(self, ctx:PrestoSQLParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#createRole.
    def visitCreateRole(self, ctx:PrestoSQLParser.CreateRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#dropRole.
    def visitDropRole(self, ctx:PrestoSQLParser.DropRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#grantRoles.
    def visitGrantRoles(self, ctx:PrestoSQLParser.GrantRolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#revokeRoles.
    def visitRevokeRoles(self, ctx:PrestoSQLParser.RevokeRolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#setRole.
    def visitSetRole(self, ctx:PrestoSQLParser.SetRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#grant.
    def visitGrant(self, ctx:PrestoSQLParser.GrantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#revoke.
    def visitRevoke(self, ctx:PrestoSQLParser.RevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showGrants.
    def visitShowGrants(self, ctx:PrestoSQLParser.ShowGrantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#explain.
    def visitExplain(self, ctx:PrestoSQLParser.ExplainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showCreateTable.
    def visitShowCreateTable(self, ctx:PrestoSQLParser.ShowCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showCreateView.
    def visitShowCreateView(self, ctx:PrestoSQLParser.ShowCreateViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showCreateFunction.
    def visitShowCreateFunction(self, ctx:PrestoSQLParser.ShowCreateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showTables.
    def visitShowTables(self, ctx:PrestoSQLParser.ShowTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showSchemas.
    def visitShowSchemas(self, ctx:PrestoSQLParser.ShowSchemasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showCatalogs.
    def visitShowCatalogs(self, ctx:PrestoSQLParser.ShowCatalogsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showColumns.
    def visitShowColumns(self, ctx:PrestoSQLParser.ShowColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showStats.
    def visitShowStats(self, ctx:PrestoSQLParser.ShowStatsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showStatsForQuery.
    def visitShowStatsForQuery(self, ctx:PrestoSQLParser.ShowStatsForQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showRoles.
    def visitShowRoles(self, ctx:PrestoSQLParser.ShowRolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showRoleGrants.
    def visitShowRoleGrants(self, ctx:PrestoSQLParser.ShowRoleGrantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showFunctions.
    def visitShowFunctions(self, ctx:PrestoSQLParser.ShowFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#showSession.
    def visitShowSession(self, ctx:PrestoSQLParser.ShowSessionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#setSession.
    def visitSetSession(self, ctx:PrestoSQLParser.SetSessionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#resetSession.
    def visitResetSession(self, ctx:PrestoSQLParser.ResetSessionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#startTransaction.
    def visitStartTransaction(self, ctx:PrestoSQLParser.StartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#commit.
    def visitCommit(self, ctx:PrestoSQLParser.CommitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#rollback.
    def visitRollback(self, ctx:PrestoSQLParser.RollbackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#prepare.
    def visitPrepare(self, ctx:PrestoSQLParser.PrepareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#deallocate.
    def visitDeallocate(self, ctx:PrestoSQLParser.DeallocateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#execute.
    def visitExecute(self, ctx:PrestoSQLParser.ExecuteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#describeInput.
    def visitDescribeInput(self, ctx:PrestoSQLParser.DescribeInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#describeOutput.
    def visitDescribeOutput(self, ctx:PrestoSQLParser.DescribeOutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#query.
    def visitQuery(self, ctx:PrestoSQLParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#r_with.
    def visitR_with(self, ctx:PrestoSQLParser.R_withContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#tableElement.
    def visitTableElement(self, ctx:PrestoSQLParser.TableElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#columnDefinition.
    def visitColumnDefinition(self, ctx:PrestoSQLParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#likeClause.
    def visitLikeClause(self, ctx:PrestoSQLParser.LikeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#properties.
    def visitProperties(self, ctx:PrestoSQLParser.PropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#r_property.
    def visitR_property(self, ctx:PrestoSQLParser.R_propertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#sqlParameterDeclaration.
    def visitSqlParameterDeclaration(self, ctx:PrestoSQLParser.SqlParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#routineCharacteristics.
    def visitRoutineCharacteristics(self, ctx:PrestoSQLParser.RoutineCharacteristicsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#routineCharacteristic.
    def visitRoutineCharacteristic(self, ctx:PrestoSQLParser.RoutineCharacteristicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#alterRoutineCharacteristics.
    def visitAlterRoutineCharacteristics(self, ctx:PrestoSQLParser.AlterRoutineCharacteristicsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#alterRoutineCharacteristic.
    def visitAlterRoutineCharacteristic(self, ctx:PrestoSQLParser.AlterRoutineCharacteristicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#routineBody.
    def visitRoutineBody(self, ctx:PrestoSQLParser.RoutineBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#returnStatement.
    def visitReturnStatement(self, ctx:PrestoSQLParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#externalBodyReference.
    def visitExternalBodyReference(self, ctx:PrestoSQLParser.ExternalBodyReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#language.
    def visitLanguage(self, ctx:PrestoSQLParser.LanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#determinism.
    def visitDeterminism(self, ctx:PrestoSQLParser.DeterminismContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#nullCallClause.
    def visitNullCallClause(self, ctx:PrestoSQLParser.NullCallClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#externalRoutineName.
    def visitExternalRoutineName(self, ctx:PrestoSQLParser.ExternalRoutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#queryNoWith.
    def visitQueryNoWith(self, ctx:PrestoSQLParser.QueryNoWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#queryTermDefault.
    def visitQueryTermDefault(self, ctx:PrestoSQLParser.QueryTermDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#setOperation.
    def visitSetOperation(self, ctx:PrestoSQLParser.SetOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#queryPrimaryDefault.
    def visitQueryPrimaryDefault(self, ctx:PrestoSQLParser.QueryPrimaryDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#table.
    def visitTable(self, ctx:PrestoSQLParser.TableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#inlineTable.
    def visitInlineTable(self, ctx:PrestoSQLParser.InlineTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#subquery.
    def visitSubquery(self, ctx:PrestoSQLParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#sortItem.
    def visitSortItem(self, ctx:PrestoSQLParser.SortItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#querySpecification.
    def visitQuerySpecification(self, ctx:PrestoSQLParser.QuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#groupBy.
    def visitGroupBy(self, ctx:PrestoSQLParser.GroupByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#singleGroupingSet.
    def visitSingleGroupingSet(self, ctx:PrestoSQLParser.SingleGroupingSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#rollup.
    def visitRollup(self, ctx:PrestoSQLParser.RollupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#cube.
    def visitCube(self, ctx:PrestoSQLParser.CubeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#multipleGroupingSets.
    def visitMultipleGroupingSets(self, ctx:PrestoSQLParser.MultipleGroupingSetsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#groupingSet.
    def visitGroupingSet(self, ctx:PrestoSQLParser.GroupingSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#namedQuery.
    def visitNamedQuery(self, ctx:PrestoSQLParser.NamedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#setQuantifier.
    def visitSetQuantifier(self, ctx:PrestoSQLParser.SetQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#selectSingle.
    def visitSelectSingle(self, ctx:PrestoSQLParser.SelectSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#selectAll.
    def visitSelectAll(self, ctx:PrestoSQLParser.SelectAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#relationDefault.
    def visitRelationDefault(self, ctx:PrestoSQLParser.RelationDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#joinRelation.
    def visitJoinRelation(self, ctx:PrestoSQLParser.JoinRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#joinType.
    def visitJoinType(self, ctx:PrestoSQLParser.JoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#joinCriteria.
    def visitJoinCriteria(self, ctx:PrestoSQLParser.JoinCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#sampledRelation.
    def visitSampledRelation(self, ctx:PrestoSQLParser.SampledRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#sampleType.
    def visitSampleType(self, ctx:PrestoSQLParser.SampleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#aliasedRelation.
    def visitAliasedRelation(self, ctx:PrestoSQLParser.AliasedRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#columnAliases.
    def visitColumnAliases(self, ctx:PrestoSQLParser.ColumnAliasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#tableName.
    def visitTableName(self, ctx:PrestoSQLParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#subqueryRelation.
    def visitSubqueryRelation(self, ctx:PrestoSQLParser.SubqueryRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#unnest.
    def visitUnnest(self, ctx:PrestoSQLParser.UnnestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#lateral.
    def visitLateral(self, ctx:PrestoSQLParser.LateralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#parenthesizedRelation.
    def visitParenthesizedRelation(self, ctx:PrestoSQLParser.ParenthesizedRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#expression.
    def visitExpression(self, ctx:PrestoSQLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#logicalNot.
    def visitLogicalNot(self, ctx:PrestoSQLParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#predicated.
    def visitPredicated(self, ctx:PrestoSQLParser.PredicatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#logicalBinary.
    def visitLogicalBinary(self, ctx:PrestoSQLParser.LogicalBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#comparison.
    def visitComparison(self, ctx:PrestoSQLParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#quantifiedComparison.
    def visitQuantifiedComparison(self, ctx:PrestoSQLParser.QuantifiedComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#between.
    def visitBetween(self, ctx:PrestoSQLParser.BetweenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#inList.
    def visitInList(self, ctx:PrestoSQLParser.InListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#inSubquery.
    def visitInSubquery(self, ctx:PrestoSQLParser.InSubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#like.
    def visitLike(self, ctx:PrestoSQLParser.LikeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#nullPredicate.
    def visitNullPredicate(self, ctx:PrestoSQLParser.NullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#distinctFrom.
    def visitDistinctFrom(self, ctx:PrestoSQLParser.DistinctFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#valueExpressionDefault.
    def visitValueExpressionDefault(self, ctx:PrestoSQLParser.ValueExpressionDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#concatenation.
    def visitConcatenation(self, ctx:PrestoSQLParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#arithmeticBinary.
    def visitArithmeticBinary(self, ctx:PrestoSQLParser.ArithmeticBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#arithmeticUnary.
    def visitArithmeticUnary(self, ctx:PrestoSQLParser.ArithmeticUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#atTimeZone.
    def visitAtTimeZone(self, ctx:PrestoSQLParser.AtTimeZoneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#dereference.
    def visitDereference(self, ctx:PrestoSQLParser.DereferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#typeConstructor.
    def visitTypeConstructor(self, ctx:PrestoSQLParser.TypeConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#specialDateTimeFunction.
    def visitSpecialDateTimeFunction(self, ctx:PrestoSQLParser.SpecialDateTimeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#substring.
    def visitSubstring(self, ctx:PrestoSQLParser.SubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#cast.
    def visitCast(self, ctx:PrestoSQLParser.CastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#lambda.
    def visitLambda(self, ctx:PrestoSQLParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:PrestoSQLParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#parameter.
    def visitParameter(self, ctx:PrestoSQLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#normalize.
    def visitNormalize(self, ctx:PrestoSQLParser.NormalizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#intervalLiteral.
    def visitIntervalLiteral(self, ctx:PrestoSQLParser.IntervalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#numericLiteral.
    def visitNumericLiteral(self, ctx:PrestoSQLParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:PrestoSQLParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#simpleCase.
    def visitSimpleCase(self, ctx:PrestoSQLParser.SimpleCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#columnReference.
    def visitColumnReference(self, ctx:PrestoSQLParser.ColumnReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#nullLiteral.
    def visitNullLiteral(self, ctx:PrestoSQLParser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#rowConstructor.
    def visitRowConstructor(self, ctx:PrestoSQLParser.RowConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#subscript.
    def visitSubscript(self, ctx:PrestoSQLParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#subqueryExpression.
    def visitSubqueryExpression(self, ctx:PrestoSQLParser.SubqueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#binaryLiteral.
    def visitBinaryLiteral(self, ctx:PrestoSQLParser.BinaryLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#currentUser.
    def visitCurrentUser(self, ctx:PrestoSQLParser.CurrentUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#extract.
    def visitExtract(self, ctx:PrestoSQLParser.ExtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#stringLiteral.
    def visitStringLiteral(self, ctx:PrestoSQLParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#arrayConstructor.
    def visitArrayConstructor(self, ctx:PrestoSQLParser.ArrayConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#functionCall.
    def visitFunctionCall(self, ctx:PrestoSQLParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#exists.
    def visitExists(self, ctx:PrestoSQLParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#position.
    def visitPosition(self, ctx:PrestoSQLParser.PositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#searchedCase.
    def visitSearchedCase(self, ctx:PrestoSQLParser.SearchedCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#groupingOperation.
    def visitGroupingOperation(self, ctx:PrestoSQLParser.GroupingOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#basicStringLiteral.
    def visitBasicStringLiteral(self, ctx:PrestoSQLParser.BasicStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#unicodeStringLiteral.
    def visitUnicodeStringLiteral(self, ctx:PrestoSQLParser.UnicodeStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#nullTreatment.
    def visitNullTreatment(self, ctx:PrestoSQLParser.NullTreatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#timeZoneInterval.
    def visitTimeZoneInterval(self, ctx:PrestoSQLParser.TimeZoneIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#timeZoneString.
    def visitTimeZoneString(self, ctx:PrestoSQLParser.TimeZoneStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:PrestoSQLParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#comparisonQuantifier.
    def visitComparisonQuantifier(self, ctx:PrestoSQLParser.ComparisonQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#booleanValue.
    def visitBooleanValue(self, ctx:PrestoSQLParser.BooleanValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#interval.
    def visitInterval(self, ctx:PrestoSQLParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#intervalField.
    def visitIntervalField(self, ctx:PrestoSQLParser.IntervalFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#normalForm.
    def visitNormalForm(self, ctx:PrestoSQLParser.NormalFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#types.
    def visitTypes(self, ctx:PrestoSQLParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#r_type.
    def visitR_type(self, ctx:PrestoSQLParser.R_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#typeParameter.
    def visitTypeParameter(self, ctx:PrestoSQLParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#baseType.
    def visitBaseType(self, ctx:PrestoSQLParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#whenClause.
    def visitWhenClause(self, ctx:PrestoSQLParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#r_filter.
    def visitR_filter(self, ctx:PrestoSQLParser.R_filterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#over.
    def visitOver(self, ctx:PrestoSQLParser.OverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#windowFrame.
    def visitWindowFrame(self, ctx:PrestoSQLParser.WindowFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#unboundedFrame.
    def visitUnboundedFrame(self, ctx:PrestoSQLParser.UnboundedFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#currentRowBound.
    def visitCurrentRowBound(self, ctx:PrestoSQLParser.CurrentRowBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#boundedFrame.
    def visitBoundedFrame(self, ctx:PrestoSQLParser.BoundedFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#explainFormat.
    def visitExplainFormat(self, ctx:PrestoSQLParser.ExplainFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#explainType.
    def visitExplainType(self, ctx:PrestoSQLParser.ExplainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#isolationLevel.
    def visitIsolationLevel(self, ctx:PrestoSQLParser.IsolationLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#transactionAccessMode.
    def visitTransactionAccessMode(self, ctx:PrestoSQLParser.TransactionAccessModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#readUncommitted.
    def visitReadUncommitted(self, ctx:PrestoSQLParser.ReadUncommittedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#readCommitted.
    def visitReadCommitted(self, ctx:PrestoSQLParser.ReadCommittedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#repeatableRead.
    def visitRepeatableRead(self, ctx:PrestoSQLParser.RepeatableReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#serializable.
    def visitSerializable(self, ctx:PrestoSQLParser.SerializableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#positionalArgument.
    def visitPositionalArgument(self, ctx:PrestoSQLParser.PositionalArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#namedArgument.
    def visitNamedArgument(self, ctx:PrestoSQLParser.NamedArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#privilege.
    def visitPrivilege(self, ctx:PrestoSQLParser.PrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#qualifiedName.
    def visitQualifiedName(self, ctx:PrestoSQLParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#currentUserGrantor.
    def visitCurrentUserGrantor(self, ctx:PrestoSQLParser.CurrentUserGrantorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#currentRoleGrantor.
    def visitCurrentRoleGrantor(self, ctx:PrestoSQLParser.CurrentRoleGrantorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#specifiedPrincipal.
    def visitSpecifiedPrincipal(self, ctx:PrestoSQLParser.SpecifiedPrincipalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#userPrincipal.
    def visitUserPrincipal(self, ctx:PrestoSQLParser.UserPrincipalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#rolePrincipal.
    def visitRolePrincipal(self, ctx:PrestoSQLParser.RolePrincipalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#unspecifiedPrincipal.
    def visitUnspecifiedPrincipal(self, ctx:PrestoSQLParser.UnspecifiedPrincipalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#roles.
    def visitRoles(self, ctx:PrestoSQLParser.RolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#unquotedIdentifier.
    def visitUnquotedIdentifier(self, ctx:PrestoSQLParser.UnquotedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#quotedIdentifier.
    def visitQuotedIdentifier(self, ctx:PrestoSQLParser.QuotedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#backQuotedIdentifier.
    def visitBackQuotedIdentifier(self, ctx:PrestoSQLParser.BackQuotedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#digitIdentifier.
    def visitDigitIdentifier(self, ctx:PrestoSQLParser.DigitIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:PrestoSQLParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#doubleLiteral.
    def visitDoubleLiteral(self, ctx:PrestoSQLParser.DoubleLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:PrestoSQLParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrestoSQLParser#nonReserved.
    def visitNonReserved(self, ctx:PrestoSQLParser.NonReservedContext):
        return self.visitChildren(ctx)



del PrestoSQLParser