import json
import sys
data_file = open("openai_finetune.json", "r").read()
ori_data = json.loads(data_file)

i = 0
for data in ori_data:
    input = "the input is: "+data["input"]
    output = data["output"]


    #转换成新的格式
    new_data = {"messages": [{"role": "system", "content": "this is a Cadence coder"},
                  {"role": "user", "content":  input},
                  {"role": "assistant", "content": output}]}

    print(json.dumps(new_data))

    i = i + 1
    # if i>1000:
    #     break