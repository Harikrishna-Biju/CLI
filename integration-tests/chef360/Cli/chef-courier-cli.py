import subprocess,json
import time
 
job_id="b9e648d7-b18b-430a-8375-b24f23bf742b"
path="/home/ubuntu/chef-integration-tests-main-2/integration-tests/chef360/automated-sleep-job/create-job-simple.json"
path2="/home/ubuntu/chef-integration-tests-main-2/integration-tests/chef360/Cli/sleep-job-2.json"
date="2024-11-21T23:59:04Z"
instanceId="dc938005-89a9-41a5-9430-fe3a0ad38978"
path3="/home/ubuntu/chef-integration-tests-main-2/integration-tests/chef360/Cli/sample.json"
profilename="random"
runId="f7a02831-4fd0-48e8-ba08-8d3725a15e16"   
profile_name=input("enter the profile name: ")
class Test_scheduler_api:
 
    # #chef-courier-cli scheduler jobs list-jobs [flags]
    def test_list_jobs(self):
        list_jobs=subprocess.run(f"chef-courier-cli scheduler jobs list-jobs",shell=True,capture_output=True)
        print(list_jobs.stdout)
        assert  list_jobs.returncode==0
 
    #Create a new new job.
    def test_add_job(self):
        add_job=subprocess.run(f"chef-courier-cli scheduler jobs add-job --body-file {path}",shell=True,capture_output=True)
        print(add_job.stdout)
        assert add_job.returncode==0  
 
    # #chef-courier-cli scheduler jobs get-pastDueJobs [flags]
    def test_pastDueJob(self):
        global date
        pastDueJOb_job=subprocess.run(f"chef-courier-cli scheduler jobs get-pastDueJobs --deadline {date}",shell=True,capture_output=True)
        print( pastDueJOb_job.stdout)
        assert  pastDueJOb_job.returncode==0  
    
    # # chef-courier-cli scheduler jobs get-job [flags]
    def test_get_job(self):
        get_job=subprocess.run(f"chef-courier-cli scheduler jobs get-job --jobId {job_id}",shell=True,capture_output=True)
        print( get_job.stdout)
        assert  get_job.returncode==0    
 
    #ask to karunesh
    #     def test_get_head():
    #     get_head=subprocess.run(f"chef-courier-cli scheduler jobs get-head --jobId {job_id}",shell=True,capture_output=True)
    #     print( get_head.stdout)
    #     assert  get_head.returncode==0  
 
    #ask update job to karunesh
        # def test_update_job():
        #     update_job=subprocess.run(f"chef-courier-cli scheduler jobs update-job --jobId {job_id}",shell=True,capture_output=True)
        #     update_job2=subprocess.run(f"chef-courier-cli scheduler jobs update-job  --body-file {path2}",shell=True,capture_output=True)
        #     print(update_job.stdout)
        #     assert update_job.returncode==0
        #     assert update_job2.returncode==0      
 
     # chef-courier-cli scheduler jobs cancel-job [flags]
    def test_cancel_job(self):
        cancel_job=subprocess.run(f"chef-courier-cli scheduler jobs cancel-job  --jobId {job_id}",shell=True,capture_output=True)
        print(cancel_job.stdout)
        assert cancel_job.returncode==0
 
    # #chef-courier-cli scheduler jobs estimate-run-times --jobId 5765e6bf-9093-4960-8236-cfd9a390381b"
    def test_estimate_run_times(self):
        estimate_run_times=subprocess.run(f"chef-courier-cli scheduler jobs estimate-run-times --jobId {job_id}",shell=True,capture_output=True)
        print(estimate_run_times.stdout)
        assert estimate_run_times.returncode==0
 
    def test_activated_job(self):
        activated_job=subprocess.run(["chef-courier-cli","scheduler","jobs","activated-job","--jobId",job_id],capture_output=True)
        print(activated_job.stdout)
        assert activated_job.returncode==0    
    
     # chef-courier-cli scheduler jobs delete-job [flags]
    def test_delete_job(self):
        delete_job=subprocess.run(f"chef-courier-cli scheduler jobs delete-job  --jobId {job_id}",shell=True,capture_output=True)
        print(delete_job.stdout)
        assert delete_job.returncode==0
 
 
 
 
 
 
 
 
 
 
 
 
 
class Test_Chef_Courier_State_Service:
    #Fetch a list of job instances, filtered by the provided query parameters. Results will contain only those records matching all provided filters.
    # def test_list_instance():
    #     result2=subprocess.run(f"chef-courier-cli state instance list-all [flags]",shell=True,capture_output=True,text=True)
    #     print(result2)
    #     assert result2.returncode==0
 
    #Captures the Job Instance and its expanded job-run list to state. This request will fail with a 500 response if both operations are not completed successfully. This allows the system to track the nodes it is expecting to hear in from, without relying on those nodes checking in to be visible. Typically invoked by Orchestrator when it is preparing to run a job instance.
    def test_create_instance(self):
        update_job=subprocess.run(f"chef-courier-cli state instance create-instance --body-file {path3} ",shell=True,capture_output=True)
        print(update_job.stdout)
        assert update_job.returncode==0
    
    #This retrieves a Job Instance record for the given instance-id. The run records associated with the Job Instance are not included in the results.
    #Note that instances that have been moved to history will not be available with this API.  
  
    def test_get_instance(self):
        update_job=subprocess.run(f"chef-courier-cli state instance get-instance --instanceId {instanceId}",shell=True,capture_output=True)
        print(update_job.stdout)
        assert update_job.returncode==0
 
    # chef-courier-cli state instance complete-instance [flags]
    def test_complete_instance(self):
        update_job=subprocess.run(f"chef-courier-cli state instance complete-instance --instanceId {instanceId}",shell=True,capture_output=True)
        print(update_job.stdout)
        assert update_job.returncode==0    
    #Retrieves all runs in the given job instance, filtered by the provided query parameters. Results returned will meet all filter criteria provided.
    def test_list_instance(self):
        result2=subprocess.run(f"chef-courier-cli state instance list-instance-runs --instanceId {instanceId}",shell=True,capture_output=True,text=True)
        print(result2)
        assert result2.returncode==0
 
    #chef-courier-cli state run get-run [flags]    
    def test_get_run(self):
        result2=subprocess.run(f"chef-courier-cli state run get-run [flags] {runId}",shell=True,capture_output=True,text=True)
        print(result2)
        assert result2.returncode==0
 
    #chef-courier-cli state run received-run [flags]
    #expected ouput not found(got conflict 409)
    def test_received_run(self):
        result2=subprocess.run(f"chef-courier-cli state run received-run --runId {runId}",shell=True,capture_output=True,text=True)  
        print(result2.stdout)
        assert result2.returncode==0  
 
    #chef-courier-cli state run timeout-run [flags]
    def test_timeout_run(self):
        result2=subprocess.run(f"chef-courier-cli state run timeout-run --runId {runId}",shell=True,capture_output=True,text=True)
        print(result2.stdout)
        assert result2.returncode==0  
 
    def test_state_complete_run(self):
        update_job=subprocess.run(f"chef-courier-cli state run complete-run --attemptNo {1} --runId {runId} --stepNo {0}",shell=True,capture_output=True)
        print(update_job.stdout)
        assert update_job.returncode==0
 
    #chef-courier-cli state run list-steps [flags]      
    def test_list_steps(self):
        result2=subprocess.run(f"chef-courier-cli state run list-steps --runId {runId}",shell=True,capture_output=True,text=True)
        print(result2.stdout)
        assert result2.returncode==0
 
    # #chef-courier-cli state run update-step [flags]
    # #  Parameters
    # # Name  Description
    # # runId *
    # # string($uuid)
    # # (path)
    # # The unique identifier of a job run in GUID format.
 
    # # pattern: [0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}
    # # stepNo *
    # # integer  
    def test_update_step(self):
        result2=subprocess.run(f"chef-courier-cli state run update-step --runId {runId} --stepNo {0}" ,shell=True,capture_output=True,text=True)
        print(result2.stdout)
        assert result2.returncode==0
    # #chef-courier-cli state run get-step-attempt-evidence [flags]
    # # Name  Description
    # # runId *
    # # string($uuid)
    # # (path)
    # #The unique identifier of a job run in GUID format.
 
    # # pattern: [0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}
    # # stepNo *
    # # integer
    # # (path)
    # # a single step/action within a job run.
 
    # # attemptNo *
    # # integer
    # # (path)
    # # the attempt number for a given step/action within a job run.
 
    def test_get_step_attempt_evidence(self):
        result2=subprocess.run(f"chef-courier-cli state run get-step-attempt-evidence --attemptNo {1} --runId {runId} --stepNo {0}",shell=True,capture_output=True,text=True)
        print(result2.stdout)
        assert result2.returncode==0         
    # #chef-courier-cli state run attach-step-attempt-evidence [flags] Parameters
    # # Name  Description
    # # runId *
    #    # string($uuid)
    # # (path)
    # #The unique identifier of a job run in GUID format.
 
    # # pattern: [0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}
    # # stepNo *
    # # integer
    # # (path)
    # # a single step/action within a job run.
 
    # # attemptNo *
    # # integer
    # # (path)
    # # the attempt number for a given step/action within a job run.
 
    def test_attach_step_attempt_evidence(self):
        result2=subprocess.run(f"chef-courier-cli state run attach-step-attempt-evidence --runId {runId}",capture_output=True,text=True)
        res7=json.loads(result2.stdout)
        runid=res7["items"][0]["runId"]
        print(res7)
        print(runid)  
 
 
        
 
 
 
 
 
 
 
 
 
 
 
    
    
    
class Test_radom_data:
    def test_job(self):
        #21-creating a job(A)and getting jobId(A)
        job_run=subprocess.run(['chef-courier-cli','scheduler','jobs','add-job','--body-file','/home/ubuntu/chef-integration-tests-main-2/integration-tests/chef360/Cli/sleep-job-2.json'],capture_output=True)
        assert job_run.returncode==0
        res5=json.loads(job_run.stdout)
        print(res5)
        global JOB_ID
        JOB_ID=res5["item"]["id"]
        print(JOB_ID)
        time.sleep(30)
    
    
    #chef-courier-cli set-default-profile [flags]
    def test_set_default_profile(self):
        update_job=subprocess.run(f"chef-courier-cli set-default-profile {profile_name}",shell=True,capture_output=True)
        print(update_job.stdout)
        assert update_job.returncode==0
    
    # chef-courier-cli state instance complete-instance [flags]
    
    instanceId="dc938005-89a9-41a5-9430-fe3a0ad38978"
    path3="/home/ubuntu/chef-integration-tests-main-2/integration-tests/chef360/Cli/sample.json"
    def test_complete_instance(self):
        update_job=subprocess.run(f"chef-courier-cli state instance complete-instance --instanceId {instanceId}",shell=True,capture_output=True)
        print(update_job.stdout)
        assert update_job.returncode==0
    
    
    # #chef-courier-cli state instance complete-instance [flags]    
    # #working
    def test_create_instance(self):
        update_job=subprocess.run(f"chef-courier-cli state instance create-instance --body-file {path3} ",shell=True,capture_output=True)
        print(update_job.stdout)
        assert update_job.returncode==0   
    
    #working
    # def test_get_instance():
    #     update_job=subprocess.run(f"chef-courier-cli state instance get-instance --instanceId {instanceId}",shell=True,capture_output=True)
    #     print(update_job.stdout)
    #assert update_job.returncode==0
    #working
    
    
 
    
    # #chef-courier-cli state run complete-run [flags]
    
    
    #pending---------->
    
    def test_state_complete_run(self):
        update_job=subprocess.run(f"chef-courier-cli state run complete-run --attemptNo {1} --runId {runId} --stepNo {0}",shell=True,capture_output=True)
        print(update_job.stdout)
        assert update_job.returncode==0
    
    # #chef-courier-cli state run get-run [flags]
    def test_state_(self):
        update_job=subprocess.run(f"chef-courier-cli state run get-run --attemptNo {1} --runId {runId} --stepNo {0}",shell=True,capture_output=True)
        print(update_job.stdout)
        assert update_job.returncode==0
    
    
    def test_get_default_profile(self):
        result2=subprocess.run(f"chef-courier-cli get-default-profile [flags]" ,shell=True,capture_output=True,text=True)
        print(result2.stdout)
        assert result2.returncode==0
    
    #not working
    # WORKSTATION_NAME="randomdemo"
    # PROFILE_NAME="random"
    # TENANT_URL="http://ec2-54-242-50-112.compute-1.amazonaws.com:31000"
    # def test_register_device():
    #       result2=subprocess.run(f"chef-platform-auth-cli register-device --device-name {WORKSTATION_NAME} --profile-name {PROFILE_NAME} --url {TENANT_URL} --insecure
    # ",shell=True,capture_output=True,text=True)
    #       print(result2.stdout)
    #       assert result2.returncode==0
    
    # deregister:
    #chef-courier-cli deregister-device [flags]

    def test_deregister_device(self):
        result2=subprocess.run(f"chef-courier-cli deregister-device --profile {profilename}" ,shell=True,capture_output=True,text=True)
        print(result2.stdout)
        assert result2.returncode==0
    
    def test_list_profile_names(self):
        result2=subprocess.run(f"chef-courier-cli list-profile-names" ,shell=True,capture_output=True,text=True)
        print(result2.stdout)
        assert result2.returncode==0
    
    # #sheduler
    # sheduler_rule="/home/ubuntu/chef-integration-tests-main-2/integration-tests/chef360/Cli/sheduler.json"
    
    # def test_list_profile_names():
    #      result2=subprocess.run(f"chef-courier-cli scheduler exceptions add-rule --body-file {sheduler_rule}" ,shell=True,capture_output=True,text=True)
    #      print(result2.stdout)
    #      assert result2.returncode==0