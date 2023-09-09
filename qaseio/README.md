# qaseio
Qase API Specification.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 3.3.0
- Build package: org.openapitools.codegen.languages.PythonPriorClientCodegen
For more information, please visit [https://qase.io](https://qase.io)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import qaseio
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import qaseio
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import qaseio
from pprint import pprint
from qaseio.api import attachments_api
from qaseio.model.attachment_list_response import AttachmentListResponse
from qaseio.model.attachment_response import AttachmentResponse
from qaseio.model.attachment_uploads_response import AttachmentUploadsResponse
from qaseio.model.hash_response import HashResponse
# Defining the host is optional and defaults to https://api.qase.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = qaseio.Configuration(
    host = "https://api.qase.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration.api_key['TokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with qaseio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attachments_api.AttachmentsApi(api_client)
    hash = "hash_example" # str | Hash.

    try:
        # Remove attachment by Hash.
        api_response = api_instance.delete_attachment(hash)
        pprint(api_response)
    except qaseio.ApiException as e:
        print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.qase.io/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttachmentsApi* | [**delete_attachment**](docs/AttachmentsApi.md#delete_attachment) | **DELETE** /attachment/{hash} | Remove attachment by Hash.
*AttachmentsApi* | [**get_attachment**](docs/AttachmentsApi.md#get_attachment) | **GET** /attachment/{hash} | Get attachment by Hash.
*AttachmentsApi* | [**get_attachments**](docs/AttachmentsApi.md#get_attachments) | **GET** /attachment | Get all attachments.
*AttachmentsApi* | [**upload_attachment**](docs/AttachmentsApi.md#upload_attachment) | **POST** /attachment/{code} | Upload attachment.
*AuthorsApi* | [**get_author**](docs/AuthorsApi.md#get_author) | **GET** /author/{id} | Get a specific author.
*AuthorsApi* | [**get_authors**](docs/AuthorsApi.md#get_authors) | **GET** /author | Get all authors.
*CasesApi* | [**bulk**](docs/CasesApi.md#bulk) | **POST** /case/{code}/bulk | Create test cases in bulk.
*CasesApi* | [**create_case**](docs/CasesApi.md#create_case) | **POST** /case/{code} | Create a new test case.
*CasesApi* | [**delete_case**](docs/CasesApi.md#delete_case) | **DELETE** /case/{code}/{id} | Delete test case.
*CasesApi* | [**get_case**](docs/CasesApi.md#get_case) | **GET** /case/{code}/{id} | Get a specific test case.
*CasesApi* | [**get_cases**](docs/CasesApi.md#get_cases) | **GET** /case/{code} | Get all test cases.
*CasesApi* | [**update_case**](docs/CasesApi.md#update_case) | **PATCH** /case/{code}/{id} | Update test case.
*CustomFieldsApi* | [**create_custom_field**](docs/CustomFieldsApi.md#create_custom_field) | **POST** /custom_field | Create new Custom Field.
*CustomFieldsApi* | [**delete_custom_field**](docs/CustomFieldsApi.md#delete_custom_field) | **DELETE** /custom_field/{id} | Delete Custom Field by id.
*CustomFieldsApi* | [**get_custom_field**](docs/CustomFieldsApi.md#get_custom_field) | **GET** /custom_field/{id} | Get Custom Field by id.
*CustomFieldsApi* | [**get_custom_fields**](docs/CustomFieldsApi.md#get_custom_fields) | **GET** /custom_field | Get all Custom Fields.
*CustomFieldsApi* | [**update_custom_field**](docs/CustomFieldsApi.md#update_custom_field) | **PATCH** /custom_field/{id} | Update Custom Field by id.
*DefectsApi* | [**create_defect**](docs/DefectsApi.md#create_defect) | **POST** /defect/{code} | Create a new defect.
*DefectsApi* | [**delete_defect**](docs/DefectsApi.md#delete_defect) | **DELETE** /defect/{code}/{id} | Delete defect.
*DefectsApi* | [**get_defect**](docs/DefectsApi.md#get_defect) | **GET** /defect/{code}/{id} | Get a specific defect.
*DefectsApi* | [**get_defects**](docs/DefectsApi.md#get_defects) | **GET** /defect/{code} | Get all defects.
*DefectsApi* | [**resolve_defect**](docs/DefectsApi.md#resolve_defect) | **PATCH** /defect/{code}/resolve/{id} | Resolve a specific defect.
*DefectsApi* | [**update_defect**](docs/DefectsApi.md#update_defect) | **PATCH** /defect/{code}/{id} | Update defect.
*DefectsApi* | [**update_defect_status**](docs/DefectsApi.md#update_defect_status) | **PATCH** /defect/{code}/status/{id} | Update a specific defect status.
*EnvironmentsApi* | [**create_environment**](docs/EnvironmentsApi.md#create_environment) | **POST** /environment/{code} | Create a new environment.
*EnvironmentsApi* | [**delete_environment**](docs/EnvironmentsApi.md#delete_environment) | **DELETE** /environment/{code}/{id} | Delete environment.
*EnvironmentsApi* | [**get_environment**](docs/EnvironmentsApi.md#get_environment) | **GET** /environment/{code}/{id} | Get a specific environment.
*EnvironmentsApi* | [**get_environments**](docs/EnvironmentsApi.md#get_environments) | **GET** /environment/{code} | Get all environments.
*EnvironmentsApi* | [**update_environment**](docs/EnvironmentsApi.md#update_environment) | **PATCH** /environment/{code}/{id} | Update environment.
*MilestonesApi* | [**create_milestone**](docs/MilestonesApi.md#create_milestone) | **POST** /milestone/{code} | Create a new milestone.
*MilestonesApi* | [**delete_milestone**](docs/MilestonesApi.md#delete_milestone) | **DELETE** /milestone/{code}/{id} | Delete milestone.
*MilestonesApi* | [**get_milestone**](docs/MilestonesApi.md#get_milestone) | **GET** /milestone/{code}/{id} | Get a specific milestone.
*MilestonesApi* | [**get_milestones**](docs/MilestonesApi.md#get_milestones) | **GET** /milestone/{code} | Get all milestones.
*MilestonesApi* | [**update_milestone**](docs/MilestonesApi.md#update_milestone) | **PATCH** /milestone/{code}/{id} | Update milestone.
*PlansApi* | [**create_plan**](docs/PlansApi.md#create_plan) | **POST** /plan/{code} | Create a new plan.
*PlansApi* | [**delete_plan**](docs/PlansApi.md#delete_plan) | **DELETE** /plan/{code}/{id} | Delete plan.
*PlansApi* | [**get_plan**](docs/PlansApi.md#get_plan) | **GET** /plan/{code}/{id} | Get a specific plan.
*PlansApi* | [**get_plans**](docs/PlansApi.md#get_plans) | **GET** /plan/{code} | Get all plans.
*PlansApi* | [**update_plan**](docs/PlansApi.md#update_plan) | **PATCH** /plan/{code}/{id} | Update plan.
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /project | Create new project.
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /project/{code} | Delete Project by code.
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /project/{code} | Get Project by code.
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /project | Get All Projects.
*ProjectsApi* | [**grant_access_to_project**](docs/ProjectsApi.md#grant_access_to_project) | **POST** /project/{code}/access | Grant access to project by code.
*ProjectsApi* | [**revoke_access_to_project**](docs/ProjectsApi.md#revoke_access_to_project) | **DELETE** /project/{code}/access | Revoke access to project by code.
*ResultApi* | [**create_results_v2**](docs/ResultApi.md#create_results_v2) | **POST** /{project_code}/run/{run_id}/results | 
*ResultsApi* | [**create_result**](docs/ResultsApi.md#create_result) | **POST** /result/{code}/{id} | Create test run result.
*ResultsApi* | [**create_result_bulk**](docs/ResultsApi.md#create_result_bulk) | **POST** /result/{code}/{id}/bulk | Bulk create test run result.
*ResultsApi* | [**delete_result**](docs/ResultsApi.md#delete_result) | **DELETE** /result/{code}/{id}/{hash} | Delete test run result.
*ResultsApi* | [**get_result**](docs/ResultsApi.md#get_result) | **GET** /result/{code}/{hash} | Get test run result by code.
*ResultsApi* | [**get_results**](docs/ResultsApi.md#get_results) | **GET** /result/{code} | Get all test run results.
*ResultsApi* | [**update_result**](docs/ResultsApi.md#update_result) | **PATCH** /result/{code}/{id}/{hash} | Update test run result.
*RunsApi* | [**complete_run**](docs/RunsApi.md#complete_run) | **POST** /run/{code}/{id}/complete | Complete a specific run.
*RunsApi* | [**create_run**](docs/RunsApi.md#create_run) | **POST** /run/{code} | Create a new run.
*RunsApi* | [**delete_run**](docs/RunsApi.md#delete_run) | **DELETE** /run/{code}/{id} | Delete run.
*RunsApi* | [**get_run**](docs/RunsApi.md#get_run) | **GET** /run/{code}/{id} | Get a specific run.
*RunsApi* | [**get_runs**](docs/RunsApi.md#get_runs) | **GET** /run/{code} | Get all runs.
*RunsApi* | [**update_run_publicity**](docs/RunsApi.md#update_run_publicity) | **PATCH** /run/{code}/{id}/public | Update publicity of a specific run.
*SearchApi* | [**search**](docs/SearchApi.md#search) | **GET** /search | Search entities by Qase Query Language (QQL).
*SharedStepsApi* | [**create_shared_step**](docs/SharedStepsApi.md#create_shared_step) | **POST** /shared_step/{code} | Create a new shared step.
*SharedStepsApi* | [**delete_shared_step**](docs/SharedStepsApi.md#delete_shared_step) | **DELETE** /shared_step/{code}/{hash} | Delete shared step.
*SharedStepsApi* | [**get_shared_step**](docs/SharedStepsApi.md#get_shared_step) | **GET** /shared_step/{code}/{hash} | Get a specific shared step.
*SharedStepsApi* | [**get_shared_steps**](docs/SharedStepsApi.md#get_shared_steps) | **GET** /shared_step/{code} | Get all shared steps.
*SharedStepsApi* | [**update_shared_step**](docs/SharedStepsApi.md#update_shared_step) | **PATCH** /shared_step/{code}/{hash} | Update shared step.
*SuitesApi* | [**create_suite**](docs/SuitesApi.md#create_suite) | **POST** /suite/{code} | Create a new test suite.
*SuitesApi* | [**delete_suite**](docs/SuitesApi.md#delete_suite) | **DELETE** /suite/{code}/{id} | Delete test suite.
*SuitesApi* | [**get_suite**](docs/SuitesApi.md#get_suite) | **GET** /suite/{code}/{id} | Get a specific test suite.
*SuitesApi* | [**get_suites**](docs/SuitesApi.md#get_suites) | **GET** /suite/{code} | Get all test suites.
*SuitesApi* | [**update_suite**](docs/SuitesApi.md#update_suite) | **PATCH** /suite/{code}/{id} | Update test suite.


## Documentation For Models

 - [Attachment](docs/Attachment.md)
 - [AttachmentGet](docs/AttachmentGet.md)
 - [AttachmentHash](docs/AttachmentHash.md)
 - [AttachmentHashList](docs/AttachmentHashList.md)
 - [AttachmentListResponse](docs/AttachmentListResponse.md)
 - [AttachmentListResponseAllOf](docs/AttachmentListResponseAllOf.md)
 - [AttachmentListResponseAllOfResult](docs/AttachmentListResponseAllOfResult.md)
 - [AttachmentResponse](docs/AttachmentResponse.md)
 - [AttachmentResponseAllOf](docs/AttachmentResponseAllOf.md)
 - [AttachmentUploadsResponse](docs/AttachmentUploadsResponse.md)
 - [AttachmentUploadsResponseAllOf](docs/AttachmentUploadsResponseAllOf.md)
 - [Author](docs/Author.md)
 - [AuthorListResponse](docs/AuthorListResponse.md)
 - [AuthorListResponseAllOf](docs/AuthorListResponseAllOf.md)
 - [AuthorListResponseAllOfResult](docs/AuthorListResponseAllOfResult.md)
 - [AuthorResponse](docs/AuthorResponse.md)
 - [AuthorResponseAllOf](docs/AuthorResponseAllOf.md)
 - [Bulk200Response](docs/Bulk200Response.md)
 - [Bulk200ResponseAllOf](docs/Bulk200ResponseAllOf.md)
 - [Bulk200ResponseAllOfResult](docs/Bulk200ResponseAllOfResult.md)
 - [BulkRequest](docs/BulkRequest.md)
 - [BulkRequestCasesInner](docs/BulkRequestCasesInner.md)
 - [BulkRequestCasesInnerAllOf](docs/BulkRequestCasesInnerAllOf.md)
 - [CreateResult200Response](docs/CreateResult200Response.md)
 - [CreateResult200ResponseAllOf](docs/CreateResult200ResponseAllOf.md)
 - [CreateResult200ResponseAllOfResult](docs/CreateResult200ResponseAllOfResult.md)
 - [CreateResultsRequestV2](docs/CreateResultsRequestV2.md)
 - [CreateResultsRequestV2ResultsInner](docs/CreateResultsRequestV2ResultsInner.md)
 - [CustomField](docs/CustomField.md)
 - [CustomFieldCreate](docs/CustomFieldCreate.md)
 - [CustomFieldCreateValueInner](docs/CustomFieldCreateValueInner.md)
 - [CustomFieldResponse](docs/CustomFieldResponse.md)
 - [CustomFieldResponseAllOf](docs/CustomFieldResponseAllOf.md)
 - [CustomFieldUpdate](docs/CustomFieldUpdate.md)
 - [CustomFieldValue](docs/CustomFieldValue.md)
 - [CustomFieldsResponse](docs/CustomFieldsResponse.md)
 - [CustomFieldsResponseAllOf](docs/CustomFieldsResponseAllOf.md)
 - [CustomFieldsResponseAllOfResult](docs/CustomFieldsResponseAllOfResult.md)
 - [Defect](docs/Defect.md)
 - [DefectCreate](docs/DefectCreate.md)
 - [DefectListResponse](docs/DefectListResponse.md)
 - [DefectListResponseAllOf](docs/DefectListResponseAllOf.md)
 - [DefectListResponseAllOfResult](docs/DefectListResponseAllOfResult.md)
 - [DefectResponse](docs/DefectResponse.md)
 - [DefectResponseAllOf](docs/DefectResponseAllOf.md)
 - [DefectStatus](docs/DefectStatus.md)
 - [DefectUpdate](docs/DefectUpdate.md)
 - [Environment](docs/Environment.md)
 - [EnvironmentCreate](docs/EnvironmentCreate.md)
 - [EnvironmentListResponse](docs/EnvironmentListResponse.md)
 - [EnvironmentListResponseAllOf](docs/EnvironmentListResponseAllOf.md)
 - [EnvironmentListResponseAllOfResult](docs/EnvironmentListResponseAllOfResult.md)
 - [EnvironmentResponse](docs/EnvironmentResponse.md)
 - [EnvironmentResponseAllOf](docs/EnvironmentResponseAllOf.md)
 - [EnvironmentUpdate](docs/EnvironmentUpdate.md)
 - [HashResponse](docs/HashResponse.md)
 - [HashResponseAllOf](docs/HashResponseAllOf.md)
 - [HashResponseAllOfResult](docs/HashResponseAllOfResult.md)
 - [IdResponse](docs/IdResponse.md)
 - [IdResponseAllOf](docs/IdResponseAllOf.md)
 - [IdResponseAllOfResult](docs/IdResponseAllOfResult.md)
 - [Milestone](docs/Milestone.md)
 - [MilestoneCreate](docs/MilestoneCreate.md)
 - [MilestoneListResponse](docs/MilestoneListResponse.md)
 - [MilestoneListResponseAllOf](docs/MilestoneListResponseAllOf.md)
 - [MilestoneListResponseAllOfResult](docs/MilestoneListResponseAllOfResult.md)
 - [MilestoneResponse](docs/MilestoneResponse.md)
 - [MilestoneResponseAllOf](docs/MilestoneResponseAllOf.md)
 - [MilestoneUpdate](docs/MilestoneUpdate.md)
 - [Plan](docs/Plan.md)
 - [PlanCreate](docs/PlanCreate.md)
 - [PlanDetailed](docs/PlanDetailed.md)
 - [PlanDetailedAllOf](docs/PlanDetailedAllOf.md)
 - [PlanDetailedAllOfCases](docs/PlanDetailedAllOfCases.md)
 - [PlanListResponse](docs/PlanListResponse.md)
 - [PlanListResponseAllOf](docs/PlanListResponseAllOf.md)
 - [PlanListResponseAllOfResult](docs/PlanListResponseAllOfResult.md)
 - [PlanResponse](docs/PlanResponse.md)
 - [PlanResponseAllOf](docs/PlanResponseAllOf.md)
 - [PlanUpdate](docs/PlanUpdate.md)
 - [Project](docs/Project.md)
 - [ProjectAccess](docs/ProjectAccess.md)
 - [ProjectCodeResponse](docs/ProjectCodeResponse.md)
 - [ProjectCodeResponseAllOf](docs/ProjectCodeResponseAllOf.md)
 - [ProjectCodeResponseAllOfResult](docs/ProjectCodeResponseAllOfResult.md)
 - [ProjectCounts](docs/ProjectCounts.md)
 - [ProjectCountsDefects](docs/ProjectCountsDefects.md)
 - [ProjectCountsRuns](docs/ProjectCountsRuns.md)
 - [ProjectCreate](docs/ProjectCreate.md)
 - [ProjectListResponse](docs/ProjectListResponse.md)
 - [ProjectListResponseAllOf](docs/ProjectListResponseAllOf.md)
 - [ProjectListResponseAllOfResult](docs/ProjectListResponseAllOfResult.md)
 - [ProjectResponse](docs/ProjectResponse.md)
 - [ProjectResponseAllOf](docs/ProjectResponseAllOf.md)
 - [QqlDefect](docs/QqlDefect.md)
 - [QqlPlan](docs/QqlPlan.md)
 - [QqlTestCase](docs/QqlTestCase.md)
 - [RelationSuite](docs/RelationSuite.md)
 - [RelationSuiteItem](docs/RelationSuiteItem.md)
 - [Requirement](docs/Requirement.md)
 - [Response](docs/Response.md)
 - [Result](docs/Result.md)
 - [ResultAttachment](docs/ResultAttachment.md)
 - [ResultCreate](docs/ResultCreate.md)
 - [ResultCreateBulk](docs/ResultCreateBulk.md)
 - [ResultCreateCase](docs/ResultCreateCase.md)
 - [ResultExecution](docs/ResultExecution.md)
 - [ResultListResponse](docs/ResultListResponse.md)
 - [ResultListResponseAllOf](docs/ResultListResponseAllOf.md)
 - [ResultListResponseAllOfResult](docs/ResultListResponseAllOfResult.md)
 - [ResultRelations](docs/ResultRelations.md)
 - [ResultResponse](docs/ResultResponse.md)
 - [ResultResponseAllOf](docs/ResultResponseAllOf.md)
 - [ResultStep](docs/ResultStep.md)
 - [ResultStepData](docs/ResultStepData.md)
 - [ResultStepExecution](docs/ResultStepExecution.md)
 - [ResultUpdate](docs/ResultUpdate.md)
 - [Run](docs/Run.md)
 - [RunCreate](docs/RunCreate.md)
 - [RunEnvironment](docs/RunEnvironment.md)
 - [RunListResponse](docs/RunListResponse.md)
 - [RunListResponseAllOf](docs/RunListResponseAllOf.md)
 - [RunListResponseAllOfResult](docs/RunListResponseAllOfResult.md)
 - [RunMilestone](docs/RunMilestone.md)
 - [RunPublic](docs/RunPublic.md)
 - [RunPublicResponse](docs/RunPublicResponse.md)
 - [RunPublicResponseAllOf](docs/RunPublicResponseAllOf.md)
 - [RunPublicResponseAllOfResult](docs/RunPublicResponseAllOfResult.md)
 - [RunResponse](docs/RunResponse.md)
 - [RunResponseAllOf](docs/RunResponseAllOf.md)
 - [RunStats](docs/RunStats.md)
 - [SearchResponse](docs/SearchResponse.md)
 - [SearchResponseAllOf](docs/SearchResponseAllOf.md)
 - [SearchResponseAllOfResult](docs/SearchResponseAllOfResult.md)
 - [SharedStep](docs/SharedStep.md)
 - [SharedStepContent](docs/SharedStepContent.md)
 - [SharedStepContentCreate](docs/SharedStepContentCreate.md)
 - [SharedStepCreate](docs/SharedStepCreate.md)
 - [SharedStepListResponse](docs/SharedStepListResponse.md)
 - [SharedStepListResponseAllOf](docs/SharedStepListResponseAllOf.md)
 - [SharedStepListResponseAllOfResult](docs/SharedStepListResponseAllOfResult.md)
 - [SharedStepResponse](docs/SharedStepResponse.md)
 - [SharedStepResponseAllOf](docs/SharedStepResponseAllOf.md)
 - [SharedStepUpdate](docs/SharedStepUpdate.md)
 - [Suite](docs/Suite.md)
 - [SuiteCreate](docs/SuiteCreate.md)
 - [SuiteDelete](docs/SuiteDelete.md)
 - [SuiteListResponse](docs/SuiteListResponse.md)
 - [SuiteListResponseAllOf](docs/SuiteListResponseAllOf.md)
 - [SuiteListResponseAllOfResult](docs/SuiteListResponseAllOfResult.md)
 - [SuiteResponse](docs/SuiteResponse.md)
 - [SuiteResponseAllOf](docs/SuiteResponseAllOf.md)
 - [SuiteUpdate](docs/SuiteUpdate.md)
 - [TagValue](docs/TagValue.md)
 - [TestCase](docs/TestCase.md)
 - [TestCaseCreate](docs/TestCaseCreate.md)
 - [TestCaseListResponse](docs/TestCaseListResponse.md)
 - [TestCaseListResponseAllOf](docs/TestCaseListResponseAllOf.md)
 - [TestCaseListResponseAllOfResult](docs/TestCaseListResponseAllOfResult.md)
 - [TestCaseParams](docs/TestCaseParams.md)
 - [TestCaseResponse](docs/TestCaseResponse.md)
 - [TestCaseResponseAllOf](docs/TestCaseResponseAllOf.md)
 - [TestCaseUpdate](docs/TestCaseUpdate.md)
 - [TestStep](docs/TestStep.md)
 - [TestStepCreate](docs/TestStepCreate.md)
 - [TestStepResult](docs/TestStepResult.md)
 - [TestStepResultCreate](docs/TestStepResultCreate.md)


## Documentation For Authorization


## TokenAuth

- **Type**: API key
- **API key parameter name**: Token
- **Location**: HTTP header


## Author

support@qase.io


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in qaseio.apis and qaseio.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from qaseio.api.default_api import DefaultApi`
- `from qaseio.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import qaseio
from qaseio.apis import *
from qaseio.models import *
```
