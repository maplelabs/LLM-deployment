# Overview

This repository shows the deployment of an LLM and an Embedding model using single-node Ray cluster.
It is expected that you're using Ubuntu-22 which has python3


# Repository Details

- LLM.py shows how to deploy Llama-2 with 13 billion parameters.  
i.e., NousResearch/Llama-2-13b-chat-hf that is fine-tuned for conversational prompts

- Embedding.py shows how to deploy an Embedding model.  
Embedding models are used to generate numerical representations of strings which help in performing semantic search.  
i.e., BAAI/bge-large-zh generates numerical arrays which captures the semantic meaning of input strings.  
Vector databases like FAISS, Redis provide the ability perform similarity searches using these embeddings.

- os_requirements.txt shows the OS packages that were installed in Ubuntu 22

- py_requirements.txt shows the Python3 requirements


# Steps

- Run the apt install command present in os_requirements.txt file

- Create virtual-environment  
   ```bash
   python3 -m venv test-venv
   ```

- Activate virtal-environment  
   ```bash
   source test-venv/bin/activate
   ```

- Install pip packages  
   ```bash
   pip install -r py_requirements.txt
   ```

- Start the single-node Ray cluster. This also starts a UI based dashboard on `YOUR-VM-IP:8265` port which you can use to explore logs, check resource utilization, and check for OOM errors etc.
  ```bash
  ray start --head --dashboard-host 0.0.0.0 --dashboard-port 8265 --num-cpus 4 --num-gpus 6
  ```

- Deploy the LLM and Embedding Apps/Actors on single-node Ray cluster
  ```bash
  serve deploy ray-config.yaml
  ```

- Other useful commands
  ```bash
  ray stop # Stop the Ray cluster
  ray status # Check the status of Ray cluster

  serve shutdown # Shutdown the current deployed Apps/Actors on Ray cluster
  serve status # Get the status of Apps/Actors currently running on Ray cluster

  python3 -m nvitop # Show the utilization of all GPUs in your system
  ```
