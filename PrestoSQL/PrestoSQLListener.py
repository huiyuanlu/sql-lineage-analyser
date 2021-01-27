# Generated from PrestoSQL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrestoSQLParser import PrestoSQLParser
else:
    from PrestoSQLParser import PrestoSQLParser

# This class defines a complete listener for a parse tree produced by PrestoSQLParser.
class PrestoSQLListener(ParseTreeListener):

    # Enter a parse tree produced by PrestoSQLParser#singleStatement.
    def enterSingleStatement(self, ctx:PrestoSQLParser.SingleStatementContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#singleStatement.
    def exitSingleStatement(self, ctx:PrestoSQLParser.SingleStatementContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#standaloneExpression.
    def enterStandaloneExpression(self, ctx:PrestoSQLParser.StandaloneExpressionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#standaloneExpression.
    def exitStandaloneExpression(self, ctx:PrestoSQLParser.StandaloneExpressionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#standaloneRoutineBody.
    def enterStandaloneRoutineBody(self, ctx:PrestoSQLParser.StandaloneRoutineBodyContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#standaloneRoutineBody.
    def exitStandaloneRoutineBody(self, ctx:PrestoSQLParser.StandaloneRoutineBodyContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#statementDefault.
    def enterStatementDefault(self, ctx:PrestoSQLParser.StatementDefaultContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#statementDefault.
    def exitStatementDefault(self, ctx:PrestoSQLParser.StatementDefaultContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#use.
    def enterUse(self, ctx:PrestoSQLParser.UseContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#use.
    def exitUse(self, ctx:PrestoSQLParser.UseContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#createSchema.
    def enterCreateSchema(self, ctx:PrestoSQLParser.CreateSchemaContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#createSchema.
    def exitCreateSchema(self, ctx:PrestoSQLParser.CreateSchemaContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#dropSchema.
    def enterDropSchema(self, ctx:PrestoSQLParser.DropSchemaContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#dropSchema.
    def exitDropSchema(self, ctx:PrestoSQLParser.DropSchemaContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#renameSchema.
    def enterRenameSchema(self, ctx:PrestoSQLParser.RenameSchemaContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#renameSchema.
    def exitRenameSchema(self, ctx:PrestoSQLParser.RenameSchemaContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#createTableAsSelect.
    def enterCreateTableAsSelect(self, ctx:PrestoSQLParser.CreateTableAsSelectContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#createTableAsSelect.
    def exitCreateTableAsSelect(self, ctx:PrestoSQLParser.CreateTableAsSelectContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#createTable.
    def enterCreateTable(self, ctx:PrestoSQLParser.CreateTableContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#createTable.
    def exitCreateTable(self, ctx:PrestoSQLParser.CreateTableContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#dropTable.
    def enterDropTable(self, ctx:PrestoSQLParser.DropTableContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#dropTable.
    def exitDropTable(self, ctx:PrestoSQLParser.DropTableContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#insertInto.
    def enterInsertInto(self, ctx:PrestoSQLParser.InsertIntoContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#insertInto.
    def exitInsertInto(self, ctx:PrestoSQLParser.InsertIntoContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#delete.
    def enterDelete(self, ctx:PrestoSQLParser.DeleteContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#delete.
    def exitDelete(self, ctx:PrestoSQLParser.DeleteContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#renameTable.
    def enterRenameTable(self, ctx:PrestoSQLParser.RenameTableContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#renameTable.
    def exitRenameTable(self, ctx:PrestoSQLParser.RenameTableContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#renameColumn.
    def enterRenameColumn(self, ctx:PrestoSQLParser.RenameColumnContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#renameColumn.
    def exitRenameColumn(self, ctx:PrestoSQLParser.RenameColumnContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#dropColumn.
    def enterDropColumn(self, ctx:PrestoSQLParser.DropColumnContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#dropColumn.
    def exitDropColumn(self, ctx:PrestoSQLParser.DropColumnContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#addColumn.
    def enterAddColumn(self, ctx:PrestoSQLParser.AddColumnContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#addColumn.
    def exitAddColumn(self, ctx:PrestoSQLParser.AddColumnContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#analyze.
    def enterAnalyze(self, ctx:PrestoSQLParser.AnalyzeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#analyze.
    def exitAnalyze(self, ctx:PrestoSQLParser.AnalyzeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#createView.
    def enterCreateView(self, ctx:PrestoSQLParser.CreateViewContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#createView.
    def exitCreateView(self, ctx:PrestoSQLParser.CreateViewContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#dropView.
    def enterDropView(self, ctx:PrestoSQLParser.DropViewContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#dropView.
    def exitDropView(self, ctx:PrestoSQLParser.DropViewContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#createFunction.
    def enterCreateFunction(self, ctx:PrestoSQLParser.CreateFunctionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#createFunction.
    def exitCreateFunction(self, ctx:PrestoSQLParser.CreateFunctionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#alterFunction.
    def enterAlterFunction(self, ctx:PrestoSQLParser.AlterFunctionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#alterFunction.
    def exitAlterFunction(self, ctx:PrestoSQLParser.AlterFunctionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#dropFunction.
    def enterDropFunction(self, ctx:PrestoSQLParser.DropFunctionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#dropFunction.
    def exitDropFunction(self, ctx:PrestoSQLParser.DropFunctionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#call.
    def enterCall(self, ctx:PrestoSQLParser.CallContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#call.
    def exitCall(self, ctx:PrestoSQLParser.CallContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#createRole.
    def enterCreateRole(self, ctx:PrestoSQLParser.CreateRoleContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#createRole.
    def exitCreateRole(self, ctx:PrestoSQLParser.CreateRoleContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#dropRole.
    def enterDropRole(self, ctx:PrestoSQLParser.DropRoleContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#dropRole.
    def exitDropRole(self, ctx:PrestoSQLParser.DropRoleContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#grantRoles.
    def enterGrantRoles(self, ctx:PrestoSQLParser.GrantRolesContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#grantRoles.
    def exitGrantRoles(self, ctx:PrestoSQLParser.GrantRolesContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#revokeRoles.
    def enterRevokeRoles(self, ctx:PrestoSQLParser.RevokeRolesContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#revokeRoles.
    def exitRevokeRoles(self, ctx:PrestoSQLParser.RevokeRolesContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#setRole.
    def enterSetRole(self, ctx:PrestoSQLParser.SetRoleContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#setRole.
    def exitSetRole(self, ctx:PrestoSQLParser.SetRoleContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#grant.
    def enterGrant(self, ctx:PrestoSQLParser.GrantContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#grant.
    def exitGrant(self, ctx:PrestoSQLParser.GrantContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#revoke.
    def enterRevoke(self, ctx:PrestoSQLParser.RevokeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#revoke.
    def exitRevoke(self, ctx:PrestoSQLParser.RevokeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showGrants.
    def enterShowGrants(self, ctx:PrestoSQLParser.ShowGrantsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showGrants.
    def exitShowGrants(self, ctx:PrestoSQLParser.ShowGrantsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#explain.
    def enterExplain(self, ctx:PrestoSQLParser.ExplainContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#explain.
    def exitExplain(self, ctx:PrestoSQLParser.ExplainContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showCreateTable.
    def enterShowCreateTable(self, ctx:PrestoSQLParser.ShowCreateTableContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showCreateTable.
    def exitShowCreateTable(self, ctx:PrestoSQLParser.ShowCreateTableContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showCreateView.
    def enterShowCreateView(self, ctx:PrestoSQLParser.ShowCreateViewContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showCreateView.
    def exitShowCreateView(self, ctx:PrestoSQLParser.ShowCreateViewContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showCreateFunction.
    def enterShowCreateFunction(self, ctx:PrestoSQLParser.ShowCreateFunctionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showCreateFunction.
    def exitShowCreateFunction(self, ctx:PrestoSQLParser.ShowCreateFunctionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showTables.
    def enterShowTables(self, ctx:PrestoSQLParser.ShowTablesContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showTables.
    def exitShowTables(self, ctx:PrestoSQLParser.ShowTablesContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showSchemas.
    def enterShowSchemas(self, ctx:PrestoSQLParser.ShowSchemasContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showSchemas.
    def exitShowSchemas(self, ctx:PrestoSQLParser.ShowSchemasContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showCatalogs.
    def enterShowCatalogs(self, ctx:PrestoSQLParser.ShowCatalogsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showCatalogs.
    def exitShowCatalogs(self, ctx:PrestoSQLParser.ShowCatalogsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showColumns.
    def enterShowColumns(self, ctx:PrestoSQLParser.ShowColumnsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showColumns.
    def exitShowColumns(self, ctx:PrestoSQLParser.ShowColumnsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showStats.
    def enterShowStats(self, ctx:PrestoSQLParser.ShowStatsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showStats.
    def exitShowStats(self, ctx:PrestoSQLParser.ShowStatsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showStatsForQuery.
    def enterShowStatsForQuery(self, ctx:PrestoSQLParser.ShowStatsForQueryContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showStatsForQuery.
    def exitShowStatsForQuery(self, ctx:PrestoSQLParser.ShowStatsForQueryContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showRoles.
    def enterShowRoles(self, ctx:PrestoSQLParser.ShowRolesContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showRoles.
    def exitShowRoles(self, ctx:PrestoSQLParser.ShowRolesContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showRoleGrants.
    def enterShowRoleGrants(self, ctx:PrestoSQLParser.ShowRoleGrantsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showRoleGrants.
    def exitShowRoleGrants(self, ctx:PrestoSQLParser.ShowRoleGrantsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showFunctions.
    def enterShowFunctions(self, ctx:PrestoSQLParser.ShowFunctionsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showFunctions.
    def exitShowFunctions(self, ctx:PrestoSQLParser.ShowFunctionsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#showSession.
    def enterShowSession(self, ctx:PrestoSQLParser.ShowSessionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#showSession.
    def exitShowSession(self, ctx:PrestoSQLParser.ShowSessionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#setSession.
    def enterSetSession(self, ctx:PrestoSQLParser.SetSessionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#setSession.
    def exitSetSession(self, ctx:PrestoSQLParser.SetSessionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#resetSession.
    def enterResetSession(self, ctx:PrestoSQLParser.ResetSessionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#resetSession.
    def exitResetSession(self, ctx:PrestoSQLParser.ResetSessionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#startTransaction.
    def enterStartTransaction(self, ctx:PrestoSQLParser.StartTransactionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#startTransaction.
    def exitStartTransaction(self, ctx:PrestoSQLParser.StartTransactionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#commit.
    def enterCommit(self, ctx:PrestoSQLParser.CommitContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#commit.
    def exitCommit(self, ctx:PrestoSQLParser.CommitContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#rollback.
    def enterRollback(self, ctx:PrestoSQLParser.RollbackContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#rollback.
    def exitRollback(self, ctx:PrestoSQLParser.RollbackContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#prepare.
    def enterPrepare(self, ctx:PrestoSQLParser.PrepareContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#prepare.
    def exitPrepare(self, ctx:PrestoSQLParser.PrepareContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#deallocate.
    def enterDeallocate(self, ctx:PrestoSQLParser.DeallocateContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#deallocate.
    def exitDeallocate(self, ctx:PrestoSQLParser.DeallocateContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#execute.
    def enterExecute(self, ctx:PrestoSQLParser.ExecuteContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#execute.
    def exitExecute(self, ctx:PrestoSQLParser.ExecuteContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#describeInput.
    def enterDescribeInput(self, ctx:PrestoSQLParser.DescribeInputContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#describeInput.
    def exitDescribeInput(self, ctx:PrestoSQLParser.DescribeInputContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#describeOutput.
    def enterDescribeOutput(self, ctx:PrestoSQLParser.DescribeOutputContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#describeOutput.
    def exitDescribeOutput(self, ctx:PrestoSQLParser.DescribeOutputContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#query.
    def enterQuery(self, ctx:PrestoSQLParser.QueryContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#query.
    def exitQuery(self, ctx:PrestoSQLParser.QueryContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#r_with.
    def enterR_with(self, ctx:PrestoSQLParser.R_withContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#r_with.
    def exitR_with(self, ctx:PrestoSQLParser.R_withContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#tableElement.
    def enterTableElement(self, ctx:PrestoSQLParser.TableElementContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#tableElement.
    def exitTableElement(self, ctx:PrestoSQLParser.TableElementContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#columnDefinition.
    def enterColumnDefinition(self, ctx:PrestoSQLParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#columnDefinition.
    def exitColumnDefinition(self, ctx:PrestoSQLParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#likeClause.
    def enterLikeClause(self, ctx:PrestoSQLParser.LikeClauseContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#likeClause.
    def exitLikeClause(self, ctx:PrestoSQLParser.LikeClauseContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#properties.
    def enterProperties(self, ctx:PrestoSQLParser.PropertiesContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#properties.
    def exitProperties(self, ctx:PrestoSQLParser.PropertiesContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#r_property.
    def enterR_property(self, ctx:PrestoSQLParser.R_propertyContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#r_property.
    def exitR_property(self, ctx:PrestoSQLParser.R_propertyContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#sqlParameterDeclaration.
    def enterSqlParameterDeclaration(self, ctx:PrestoSQLParser.SqlParameterDeclarationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#sqlParameterDeclaration.
    def exitSqlParameterDeclaration(self, ctx:PrestoSQLParser.SqlParameterDeclarationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#routineCharacteristics.
    def enterRoutineCharacteristics(self, ctx:PrestoSQLParser.RoutineCharacteristicsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#routineCharacteristics.
    def exitRoutineCharacteristics(self, ctx:PrestoSQLParser.RoutineCharacteristicsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#routineCharacteristic.
    def enterRoutineCharacteristic(self, ctx:PrestoSQLParser.RoutineCharacteristicContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#routineCharacteristic.
    def exitRoutineCharacteristic(self, ctx:PrestoSQLParser.RoutineCharacteristicContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#alterRoutineCharacteristics.
    def enterAlterRoutineCharacteristics(self, ctx:PrestoSQLParser.AlterRoutineCharacteristicsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#alterRoutineCharacteristics.
    def exitAlterRoutineCharacteristics(self, ctx:PrestoSQLParser.AlterRoutineCharacteristicsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#alterRoutineCharacteristic.
    def enterAlterRoutineCharacteristic(self, ctx:PrestoSQLParser.AlterRoutineCharacteristicContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#alterRoutineCharacteristic.
    def exitAlterRoutineCharacteristic(self, ctx:PrestoSQLParser.AlterRoutineCharacteristicContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#routineBody.
    def enterRoutineBody(self, ctx:PrestoSQLParser.RoutineBodyContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#routineBody.
    def exitRoutineBody(self, ctx:PrestoSQLParser.RoutineBodyContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#returnStatement.
    def enterReturnStatement(self, ctx:PrestoSQLParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#returnStatement.
    def exitReturnStatement(self, ctx:PrestoSQLParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#externalBodyReference.
    def enterExternalBodyReference(self, ctx:PrestoSQLParser.ExternalBodyReferenceContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#externalBodyReference.
    def exitExternalBodyReference(self, ctx:PrestoSQLParser.ExternalBodyReferenceContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#language.
    def enterLanguage(self, ctx:PrestoSQLParser.LanguageContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#language.
    def exitLanguage(self, ctx:PrestoSQLParser.LanguageContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#determinism.
    def enterDeterminism(self, ctx:PrestoSQLParser.DeterminismContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#determinism.
    def exitDeterminism(self, ctx:PrestoSQLParser.DeterminismContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#nullCallClause.
    def enterNullCallClause(self, ctx:PrestoSQLParser.NullCallClauseContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#nullCallClause.
    def exitNullCallClause(self, ctx:PrestoSQLParser.NullCallClauseContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#externalRoutineName.
    def enterExternalRoutineName(self, ctx:PrestoSQLParser.ExternalRoutineNameContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#externalRoutineName.
    def exitExternalRoutineName(self, ctx:PrestoSQLParser.ExternalRoutineNameContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#queryNoWith.
    def enterQueryNoWith(self, ctx:PrestoSQLParser.QueryNoWithContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#queryNoWith.
    def exitQueryNoWith(self, ctx:PrestoSQLParser.QueryNoWithContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#queryTermDefault.
    def enterQueryTermDefault(self, ctx:PrestoSQLParser.QueryTermDefaultContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#queryTermDefault.
    def exitQueryTermDefault(self, ctx:PrestoSQLParser.QueryTermDefaultContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#setOperation.
    def enterSetOperation(self, ctx:PrestoSQLParser.SetOperationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#setOperation.
    def exitSetOperation(self, ctx:PrestoSQLParser.SetOperationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#queryPrimaryDefault.
    def enterQueryPrimaryDefault(self, ctx:PrestoSQLParser.QueryPrimaryDefaultContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#queryPrimaryDefault.
    def exitQueryPrimaryDefault(self, ctx:PrestoSQLParser.QueryPrimaryDefaultContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#table.
    def enterTable(self, ctx:PrestoSQLParser.TableContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#table.
    def exitTable(self, ctx:PrestoSQLParser.TableContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#inlineTable.
    def enterInlineTable(self, ctx:PrestoSQLParser.InlineTableContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#inlineTable.
    def exitInlineTable(self, ctx:PrestoSQLParser.InlineTableContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#subquery.
    def enterSubquery(self, ctx:PrestoSQLParser.SubqueryContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#subquery.
    def exitSubquery(self, ctx:PrestoSQLParser.SubqueryContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#sortItem.
    def enterSortItem(self, ctx:PrestoSQLParser.SortItemContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#sortItem.
    def exitSortItem(self, ctx:PrestoSQLParser.SortItemContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#querySpecification.
    def enterQuerySpecification(self, ctx:PrestoSQLParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#querySpecification.
    def exitQuerySpecification(self, ctx:PrestoSQLParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#groupBy.
    def enterGroupBy(self, ctx:PrestoSQLParser.GroupByContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#groupBy.
    def exitGroupBy(self, ctx:PrestoSQLParser.GroupByContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#singleGroupingSet.
    def enterSingleGroupingSet(self, ctx:PrestoSQLParser.SingleGroupingSetContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#singleGroupingSet.
    def exitSingleGroupingSet(self, ctx:PrestoSQLParser.SingleGroupingSetContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#rollup.
    def enterRollup(self, ctx:PrestoSQLParser.RollupContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#rollup.
    def exitRollup(self, ctx:PrestoSQLParser.RollupContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#cube.
    def enterCube(self, ctx:PrestoSQLParser.CubeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#cube.
    def exitCube(self, ctx:PrestoSQLParser.CubeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#multipleGroupingSets.
    def enterMultipleGroupingSets(self, ctx:PrestoSQLParser.MultipleGroupingSetsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#multipleGroupingSets.
    def exitMultipleGroupingSets(self, ctx:PrestoSQLParser.MultipleGroupingSetsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#groupingSet.
    def enterGroupingSet(self, ctx:PrestoSQLParser.GroupingSetContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#groupingSet.
    def exitGroupingSet(self, ctx:PrestoSQLParser.GroupingSetContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#namedQuery.
    def enterNamedQuery(self, ctx:PrestoSQLParser.NamedQueryContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#namedQuery.
    def exitNamedQuery(self, ctx:PrestoSQLParser.NamedQueryContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#setQuantifier.
    def enterSetQuantifier(self, ctx:PrestoSQLParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#setQuantifier.
    def exitSetQuantifier(self, ctx:PrestoSQLParser.SetQuantifierContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#selectSingle.
    def enterSelectSingle(self, ctx:PrestoSQLParser.SelectSingleContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#selectSingle.
    def exitSelectSingle(self, ctx:PrestoSQLParser.SelectSingleContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#selectAll.
    def enterSelectAll(self, ctx:PrestoSQLParser.SelectAllContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#selectAll.
    def exitSelectAll(self, ctx:PrestoSQLParser.SelectAllContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#relationDefault.
    def enterRelationDefault(self, ctx:PrestoSQLParser.RelationDefaultContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#relationDefault.
    def exitRelationDefault(self, ctx:PrestoSQLParser.RelationDefaultContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#joinRelation.
    def enterJoinRelation(self, ctx:PrestoSQLParser.JoinRelationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#joinRelation.
    def exitJoinRelation(self, ctx:PrestoSQLParser.JoinRelationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#joinType.
    def enterJoinType(self, ctx:PrestoSQLParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#joinType.
    def exitJoinType(self, ctx:PrestoSQLParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#joinCriteria.
    def enterJoinCriteria(self, ctx:PrestoSQLParser.JoinCriteriaContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#joinCriteria.
    def exitJoinCriteria(self, ctx:PrestoSQLParser.JoinCriteriaContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#sampledRelation.
    def enterSampledRelation(self, ctx:PrestoSQLParser.SampledRelationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#sampledRelation.
    def exitSampledRelation(self, ctx:PrestoSQLParser.SampledRelationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#sampleType.
    def enterSampleType(self, ctx:PrestoSQLParser.SampleTypeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#sampleType.
    def exitSampleType(self, ctx:PrestoSQLParser.SampleTypeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#aliasedRelation.
    def enterAliasedRelation(self, ctx:PrestoSQLParser.AliasedRelationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#aliasedRelation.
    def exitAliasedRelation(self, ctx:PrestoSQLParser.AliasedRelationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#columnAliases.
    def enterColumnAliases(self, ctx:PrestoSQLParser.ColumnAliasesContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#columnAliases.
    def exitColumnAliases(self, ctx:PrestoSQLParser.ColumnAliasesContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#tableName.
    def enterTableName(self, ctx:PrestoSQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#tableName.
    def exitTableName(self, ctx:PrestoSQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#subqueryRelation.
    def enterSubqueryRelation(self, ctx:PrestoSQLParser.SubqueryRelationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#subqueryRelation.
    def exitSubqueryRelation(self, ctx:PrestoSQLParser.SubqueryRelationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#unnest.
    def enterUnnest(self, ctx:PrestoSQLParser.UnnestContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#unnest.
    def exitUnnest(self, ctx:PrestoSQLParser.UnnestContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#lateral.
    def enterLateral(self, ctx:PrestoSQLParser.LateralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#lateral.
    def exitLateral(self, ctx:PrestoSQLParser.LateralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#parenthesizedRelation.
    def enterParenthesizedRelation(self, ctx:PrestoSQLParser.ParenthesizedRelationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#parenthesizedRelation.
    def exitParenthesizedRelation(self, ctx:PrestoSQLParser.ParenthesizedRelationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#expression.
    def enterExpression(self, ctx:PrestoSQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#expression.
    def exitExpression(self, ctx:PrestoSQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#logicalNot.
    def enterLogicalNot(self, ctx:PrestoSQLParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#logicalNot.
    def exitLogicalNot(self, ctx:PrestoSQLParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#predicated.
    def enterPredicated(self, ctx:PrestoSQLParser.PredicatedContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#predicated.
    def exitPredicated(self, ctx:PrestoSQLParser.PredicatedContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#logicalBinary.
    def enterLogicalBinary(self, ctx:PrestoSQLParser.LogicalBinaryContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#logicalBinary.
    def exitLogicalBinary(self, ctx:PrestoSQLParser.LogicalBinaryContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#comparison.
    def enterComparison(self, ctx:PrestoSQLParser.ComparisonContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#comparison.
    def exitComparison(self, ctx:PrestoSQLParser.ComparisonContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#quantifiedComparison.
    def enterQuantifiedComparison(self, ctx:PrestoSQLParser.QuantifiedComparisonContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#quantifiedComparison.
    def exitQuantifiedComparison(self, ctx:PrestoSQLParser.QuantifiedComparisonContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#between.
    def enterBetween(self, ctx:PrestoSQLParser.BetweenContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#between.
    def exitBetween(self, ctx:PrestoSQLParser.BetweenContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#inList.
    def enterInList(self, ctx:PrestoSQLParser.InListContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#inList.
    def exitInList(self, ctx:PrestoSQLParser.InListContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#inSubquery.
    def enterInSubquery(self, ctx:PrestoSQLParser.InSubqueryContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#inSubquery.
    def exitInSubquery(self, ctx:PrestoSQLParser.InSubqueryContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#like.
    def enterLike(self, ctx:PrestoSQLParser.LikeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#like.
    def exitLike(self, ctx:PrestoSQLParser.LikeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#nullPredicate.
    def enterNullPredicate(self, ctx:PrestoSQLParser.NullPredicateContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#nullPredicate.
    def exitNullPredicate(self, ctx:PrestoSQLParser.NullPredicateContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#distinctFrom.
    def enterDistinctFrom(self, ctx:PrestoSQLParser.DistinctFromContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#distinctFrom.
    def exitDistinctFrom(self, ctx:PrestoSQLParser.DistinctFromContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#valueExpressionDefault.
    def enterValueExpressionDefault(self, ctx:PrestoSQLParser.ValueExpressionDefaultContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#valueExpressionDefault.
    def exitValueExpressionDefault(self, ctx:PrestoSQLParser.ValueExpressionDefaultContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#concatenation.
    def enterConcatenation(self, ctx:PrestoSQLParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#concatenation.
    def exitConcatenation(self, ctx:PrestoSQLParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#arithmeticBinary.
    def enterArithmeticBinary(self, ctx:PrestoSQLParser.ArithmeticBinaryContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#arithmeticBinary.
    def exitArithmeticBinary(self, ctx:PrestoSQLParser.ArithmeticBinaryContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#arithmeticUnary.
    def enterArithmeticUnary(self, ctx:PrestoSQLParser.ArithmeticUnaryContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#arithmeticUnary.
    def exitArithmeticUnary(self, ctx:PrestoSQLParser.ArithmeticUnaryContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#atTimeZone.
    def enterAtTimeZone(self, ctx:PrestoSQLParser.AtTimeZoneContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#atTimeZone.
    def exitAtTimeZone(self, ctx:PrestoSQLParser.AtTimeZoneContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#dereference.
    def enterDereference(self, ctx:PrestoSQLParser.DereferenceContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#dereference.
    def exitDereference(self, ctx:PrestoSQLParser.DereferenceContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#typeConstructor.
    def enterTypeConstructor(self, ctx:PrestoSQLParser.TypeConstructorContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#typeConstructor.
    def exitTypeConstructor(self, ctx:PrestoSQLParser.TypeConstructorContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#specialDateTimeFunction.
    def enterSpecialDateTimeFunction(self, ctx:PrestoSQLParser.SpecialDateTimeFunctionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#specialDateTimeFunction.
    def exitSpecialDateTimeFunction(self, ctx:PrestoSQLParser.SpecialDateTimeFunctionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#substring.
    def enterSubstring(self, ctx:PrestoSQLParser.SubstringContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#substring.
    def exitSubstring(self, ctx:PrestoSQLParser.SubstringContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#cast.
    def enterCast(self, ctx:PrestoSQLParser.CastContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#cast.
    def exitCast(self, ctx:PrestoSQLParser.CastContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#lambda.
    def enterLambda(self, ctx:PrestoSQLParser.LambdaContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#lambda.
    def exitLambda(self, ctx:PrestoSQLParser.LambdaContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:PrestoSQLParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:PrestoSQLParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#parameter.
    def enterParameter(self, ctx:PrestoSQLParser.ParameterContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#parameter.
    def exitParameter(self, ctx:PrestoSQLParser.ParameterContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#normalize.
    def enterNormalize(self, ctx:PrestoSQLParser.NormalizeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#normalize.
    def exitNormalize(self, ctx:PrestoSQLParser.NormalizeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#intervalLiteral.
    def enterIntervalLiteral(self, ctx:PrestoSQLParser.IntervalLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#intervalLiteral.
    def exitIntervalLiteral(self, ctx:PrestoSQLParser.IntervalLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#numericLiteral.
    def enterNumericLiteral(self, ctx:PrestoSQLParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#numericLiteral.
    def exitNumericLiteral(self, ctx:PrestoSQLParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:PrestoSQLParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:PrestoSQLParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#simpleCase.
    def enterSimpleCase(self, ctx:PrestoSQLParser.SimpleCaseContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#simpleCase.
    def exitSimpleCase(self, ctx:PrestoSQLParser.SimpleCaseContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#columnReference.
    def enterColumnReference(self, ctx:PrestoSQLParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#columnReference.
    def exitColumnReference(self, ctx:PrestoSQLParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#nullLiteral.
    def enterNullLiteral(self, ctx:PrestoSQLParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#nullLiteral.
    def exitNullLiteral(self, ctx:PrestoSQLParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#rowConstructor.
    def enterRowConstructor(self, ctx:PrestoSQLParser.RowConstructorContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#rowConstructor.
    def exitRowConstructor(self, ctx:PrestoSQLParser.RowConstructorContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#subscript.
    def enterSubscript(self, ctx:PrestoSQLParser.SubscriptContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#subscript.
    def exitSubscript(self, ctx:PrestoSQLParser.SubscriptContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#subqueryExpression.
    def enterSubqueryExpression(self, ctx:PrestoSQLParser.SubqueryExpressionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#subqueryExpression.
    def exitSubqueryExpression(self, ctx:PrestoSQLParser.SubqueryExpressionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#binaryLiteral.
    def enterBinaryLiteral(self, ctx:PrestoSQLParser.BinaryLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#binaryLiteral.
    def exitBinaryLiteral(self, ctx:PrestoSQLParser.BinaryLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#currentUser.
    def enterCurrentUser(self, ctx:PrestoSQLParser.CurrentUserContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#currentUser.
    def exitCurrentUser(self, ctx:PrestoSQLParser.CurrentUserContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#extract.
    def enterExtract(self, ctx:PrestoSQLParser.ExtractContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#extract.
    def exitExtract(self, ctx:PrestoSQLParser.ExtractContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#stringLiteral.
    def enterStringLiteral(self, ctx:PrestoSQLParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#stringLiteral.
    def exitStringLiteral(self, ctx:PrestoSQLParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#arrayConstructor.
    def enterArrayConstructor(self, ctx:PrestoSQLParser.ArrayConstructorContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#arrayConstructor.
    def exitArrayConstructor(self, ctx:PrestoSQLParser.ArrayConstructorContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#functionCall.
    def enterFunctionCall(self, ctx:PrestoSQLParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#functionCall.
    def exitFunctionCall(self, ctx:PrestoSQLParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#exists.
    def enterExists(self, ctx:PrestoSQLParser.ExistsContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#exists.
    def exitExists(self, ctx:PrestoSQLParser.ExistsContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#position.
    def enterPosition(self, ctx:PrestoSQLParser.PositionContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#position.
    def exitPosition(self, ctx:PrestoSQLParser.PositionContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#searchedCase.
    def enterSearchedCase(self, ctx:PrestoSQLParser.SearchedCaseContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#searchedCase.
    def exitSearchedCase(self, ctx:PrestoSQLParser.SearchedCaseContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#groupingOperation.
    def enterGroupingOperation(self, ctx:PrestoSQLParser.GroupingOperationContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#groupingOperation.
    def exitGroupingOperation(self, ctx:PrestoSQLParser.GroupingOperationContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#basicStringLiteral.
    def enterBasicStringLiteral(self, ctx:PrestoSQLParser.BasicStringLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#basicStringLiteral.
    def exitBasicStringLiteral(self, ctx:PrestoSQLParser.BasicStringLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#unicodeStringLiteral.
    def enterUnicodeStringLiteral(self, ctx:PrestoSQLParser.UnicodeStringLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#unicodeStringLiteral.
    def exitUnicodeStringLiteral(self, ctx:PrestoSQLParser.UnicodeStringLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#nullTreatment.
    def enterNullTreatment(self, ctx:PrestoSQLParser.NullTreatmentContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#nullTreatment.
    def exitNullTreatment(self, ctx:PrestoSQLParser.NullTreatmentContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#timeZoneInterval.
    def enterTimeZoneInterval(self, ctx:PrestoSQLParser.TimeZoneIntervalContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#timeZoneInterval.
    def exitTimeZoneInterval(self, ctx:PrestoSQLParser.TimeZoneIntervalContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#timeZoneString.
    def enterTimeZoneString(self, ctx:PrestoSQLParser.TimeZoneStringContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#timeZoneString.
    def exitTimeZoneString(self, ctx:PrestoSQLParser.TimeZoneStringContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:PrestoSQLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:PrestoSQLParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#comparisonQuantifier.
    def enterComparisonQuantifier(self, ctx:PrestoSQLParser.ComparisonQuantifierContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#comparisonQuantifier.
    def exitComparisonQuantifier(self, ctx:PrestoSQLParser.ComparisonQuantifierContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#booleanValue.
    def enterBooleanValue(self, ctx:PrestoSQLParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#booleanValue.
    def exitBooleanValue(self, ctx:PrestoSQLParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#interval.
    def enterInterval(self, ctx:PrestoSQLParser.IntervalContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#interval.
    def exitInterval(self, ctx:PrestoSQLParser.IntervalContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#intervalField.
    def enterIntervalField(self, ctx:PrestoSQLParser.IntervalFieldContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#intervalField.
    def exitIntervalField(self, ctx:PrestoSQLParser.IntervalFieldContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#normalForm.
    def enterNormalForm(self, ctx:PrestoSQLParser.NormalFormContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#normalForm.
    def exitNormalForm(self, ctx:PrestoSQLParser.NormalFormContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#types.
    def enterTypes(self, ctx:PrestoSQLParser.TypesContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#types.
    def exitTypes(self, ctx:PrestoSQLParser.TypesContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#r_type.
    def enterR_type(self, ctx:PrestoSQLParser.R_typeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#r_type.
    def exitR_type(self, ctx:PrestoSQLParser.R_typeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#typeParameter.
    def enterTypeParameter(self, ctx:PrestoSQLParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#typeParameter.
    def exitTypeParameter(self, ctx:PrestoSQLParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#baseType.
    def enterBaseType(self, ctx:PrestoSQLParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#baseType.
    def exitBaseType(self, ctx:PrestoSQLParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#whenClause.
    def enterWhenClause(self, ctx:PrestoSQLParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#whenClause.
    def exitWhenClause(self, ctx:PrestoSQLParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#r_filter.
    def enterR_filter(self, ctx:PrestoSQLParser.R_filterContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#r_filter.
    def exitR_filter(self, ctx:PrestoSQLParser.R_filterContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#over.
    def enterOver(self, ctx:PrestoSQLParser.OverContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#over.
    def exitOver(self, ctx:PrestoSQLParser.OverContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#windowFrame.
    def enterWindowFrame(self, ctx:PrestoSQLParser.WindowFrameContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#windowFrame.
    def exitWindowFrame(self, ctx:PrestoSQLParser.WindowFrameContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#unboundedFrame.
    def enterUnboundedFrame(self, ctx:PrestoSQLParser.UnboundedFrameContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#unboundedFrame.
    def exitUnboundedFrame(self, ctx:PrestoSQLParser.UnboundedFrameContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#currentRowBound.
    def enterCurrentRowBound(self, ctx:PrestoSQLParser.CurrentRowBoundContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#currentRowBound.
    def exitCurrentRowBound(self, ctx:PrestoSQLParser.CurrentRowBoundContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#boundedFrame.
    def enterBoundedFrame(self, ctx:PrestoSQLParser.BoundedFrameContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#boundedFrame.
    def exitBoundedFrame(self, ctx:PrestoSQLParser.BoundedFrameContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#explainFormat.
    def enterExplainFormat(self, ctx:PrestoSQLParser.ExplainFormatContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#explainFormat.
    def exitExplainFormat(self, ctx:PrestoSQLParser.ExplainFormatContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#explainType.
    def enterExplainType(self, ctx:PrestoSQLParser.ExplainTypeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#explainType.
    def exitExplainType(self, ctx:PrestoSQLParser.ExplainTypeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#isolationLevel.
    def enterIsolationLevel(self, ctx:PrestoSQLParser.IsolationLevelContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#isolationLevel.
    def exitIsolationLevel(self, ctx:PrestoSQLParser.IsolationLevelContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#transactionAccessMode.
    def enterTransactionAccessMode(self, ctx:PrestoSQLParser.TransactionAccessModeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#transactionAccessMode.
    def exitTransactionAccessMode(self, ctx:PrestoSQLParser.TransactionAccessModeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#readUncommitted.
    def enterReadUncommitted(self, ctx:PrestoSQLParser.ReadUncommittedContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#readUncommitted.
    def exitReadUncommitted(self, ctx:PrestoSQLParser.ReadUncommittedContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#readCommitted.
    def enterReadCommitted(self, ctx:PrestoSQLParser.ReadCommittedContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#readCommitted.
    def exitReadCommitted(self, ctx:PrestoSQLParser.ReadCommittedContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#repeatableRead.
    def enterRepeatableRead(self, ctx:PrestoSQLParser.RepeatableReadContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#repeatableRead.
    def exitRepeatableRead(self, ctx:PrestoSQLParser.RepeatableReadContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#serializable.
    def enterSerializable(self, ctx:PrestoSQLParser.SerializableContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#serializable.
    def exitSerializable(self, ctx:PrestoSQLParser.SerializableContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#positionalArgument.
    def enterPositionalArgument(self, ctx:PrestoSQLParser.PositionalArgumentContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#positionalArgument.
    def exitPositionalArgument(self, ctx:PrestoSQLParser.PositionalArgumentContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#namedArgument.
    def enterNamedArgument(self, ctx:PrestoSQLParser.NamedArgumentContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#namedArgument.
    def exitNamedArgument(self, ctx:PrestoSQLParser.NamedArgumentContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#privilege.
    def enterPrivilege(self, ctx:PrestoSQLParser.PrivilegeContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#privilege.
    def exitPrivilege(self, ctx:PrestoSQLParser.PrivilegeContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#qualifiedName.
    def enterQualifiedName(self, ctx:PrestoSQLParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#qualifiedName.
    def exitQualifiedName(self, ctx:PrestoSQLParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#currentUserGrantor.
    def enterCurrentUserGrantor(self, ctx:PrestoSQLParser.CurrentUserGrantorContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#currentUserGrantor.
    def exitCurrentUserGrantor(self, ctx:PrestoSQLParser.CurrentUserGrantorContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#currentRoleGrantor.
    def enterCurrentRoleGrantor(self, ctx:PrestoSQLParser.CurrentRoleGrantorContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#currentRoleGrantor.
    def exitCurrentRoleGrantor(self, ctx:PrestoSQLParser.CurrentRoleGrantorContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#specifiedPrincipal.
    def enterSpecifiedPrincipal(self, ctx:PrestoSQLParser.SpecifiedPrincipalContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#specifiedPrincipal.
    def exitSpecifiedPrincipal(self, ctx:PrestoSQLParser.SpecifiedPrincipalContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#userPrincipal.
    def enterUserPrincipal(self, ctx:PrestoSQLParser.UserPrincipalContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#userPrincipal.
    def exitUserPrincipal(self, ctx:PrestoSQLParser.UserPrincipalContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#rolePrincipal.
    def enterRolePrincipal(self, ctx:PrestoSQLParser.RolePrincipalContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#rolePrincipal.
    def exitRolePrincipal(self, ctx:PrestoSQLParser.RolePrincipalContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#unspecifiedPrincipal.
    def enterUnspecifiedPrincipal(self, ctx:PrestoSQLParser.UnspecifiedPrincipalContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#unspecifiedPrincipal.
    def exitUnspecifiedPrincipal(self, ctx:PrestoSQLParser.UnspecifiedPrincipalContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#roles.
    def enterRoles(self, ctx:PrestoSQLParser.RolesContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#roles.
    def exitRoles(self, ctx:PrestoSQLParser.RolesContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#unquotedIdentifier.
    def enterUnquotedIdentifier(self, ctx:PrestoSQLParser.UnquotedIdentifierContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#unquotedIdentifier.
    def exitUnquotedIdentifier(self, ctx:PrestoSQLParser.UnquotedIdentifierContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#quotedIdentifier.
    def enterQuotedIdentifier(self, ctx:PrestoSQLParser.QuotedIdentifierContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#quotedIdentifier.
    def exitQuotedIdentifier(self, ctx:PrestoSQLParser.QuotedIdentifierContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#backQuotedIdentifier.
    def enterBackQuotedIdentifier(self, ctx:PrestoSQLParser.BackQuotedIdentifierContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#backQuotedIdentifier.
    def exitBackQuotedIdentifier(self, ctx:PrestoSQLParser.BackQuotedIdentifierContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#digitIdentifier.
    def enterDigitIdentifier(self, ctx:PrestoSQLParser.DigitIdentifierContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#digitIdentifier.
    def exitDigitIdentifier(self, ctx:PrestoSQLParser.DigitIdentifierContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:PrestoSQLParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:PrestoSQLParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#doubleLiteral.
    def enterDoubleLiteral(self, ctx:PrestoSQLParser.DoubleLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#doubleLiteral.
    def exitDoubleLiteral(self, ctx:PrestoSQLParser.DoubleLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:PrestoSQLParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:PrestoSQLParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by PrestoSQLParser#nonReserved.
    def enterNonReserved(self, ctx:PrestoSQLParser.NonReservedContext):
        pass

    # Exit a parse tree produced by PrestoSQLParser#nonReserved.
    def exitNonReserved(self, ctx:PrestoSQLParser.NonReservedContext):
        pass



del PrestoSQLParser