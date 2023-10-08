import os
import time
import openai
#模型微调
#pip3 install --upgrade openai

openai.api_key = "sk-******"

#step 1, upload file
ret = openai.File.create(
  file=open("code_all.jsonl", "rb"),
  purpose='fine-tune'
)
print(ret)
file_id = ret["id"] #file-Ehp7Pf6FDLaofvTwNzxVBc9w
print("file_id", file_id) #file_id = "file-aSNRVFIfqoJNk327t8TsbRm3"
time.sleep(10*60)


#step 2, build the tune job
ret = openai.FineTuningJob.create(training_file=file_id, model="gpt-3.5-turbo")
print(ret)
job_id = ret["id"] #
print(job_id)  #job_id = "ftjob-LYJsaV8knoxZOeMGxpu6jmpx"

time.sleep(3*60)

#step 3,wait training finish
# Retrieve the state of a fine-tune
for i in range(1000):
    ret = openai.FineTuningJob.retrieve(job_id)
    #print(ret)
    print(ret["status"], ret["fine_tuned_model"]) #ft:gpt-3.5-turbo-0613:personal::7w7keItl
    if "succeeded" == ret["status"]:
        break

    time.sleep(60)

