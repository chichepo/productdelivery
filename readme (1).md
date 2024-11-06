# Product Delivery Pipeline<p></p>
<p>This project implements a configurable product delivery pipeline that can build, deploy, and notify about various products.</p>
<h2>Project structure</h2>
<p>The project structure looks like this:</p>
<pre><code>productdelivery/
├── .gitignore
├── README.md
├── requirements.txt
├── config.json
└── pipeline.py
</code></pre>
<h2>Features</h2>
<ul>
<li><p>Configurable product pipelines</p>
</li><li><p>Support for multiple deployment targets (Artifactory, Nexus, S3)</p>
</li><li><p>Support for multiple notification channels (Email, Slack)</p>
</li></ul>
<h2>Usage</h2>
<ol>
<li><p>Update the <code>config.json</code> file with your product configurations.</p>
</li><li><p>Run the pipeline with: <code>python pipeline.py</code></p>
</li></ol>
<h2>Configuration</h2>
<p>The <code>config.json</code> file should contain an array of products, each with:</p>
<ul>
<li><p>name: Product name</p>
</li><li><p>scheduled_time: Time to run the pipeline</p>
</li><li><p>deploy_targets: List of deployment targets</p>
</li><li><p>notification_channels: List of notification channels</p>
</li></ul>
<p>Example:</p>
<pre><code class="language-json">{
  "products": [
    {
      "name": "ProductA",
      "scheduled_time": "10:00",
      "deploy_targets": ["Artifactory", "S3"],
      "notification_channels": ["Email", "Slack"]
    }
  ]
}
</code></pre>
<h2>Setting up the Virtual Environment</h2>

<p>To isolate the project dependencies, it's recommended to use a virtual environment. Here's how to set it up:</p>

<ol>
  <li>
    <p>Open a terminal and navigate to your project directory:</p>
    <pre><code>cd path/to/productdelivery</code></pre>
  </li>

  <li>
    <p>Create a new virtual environment:</p>
    <pre><code>python -m venv venv</code></pre>
  </li>

  <li>
    <p>Activate the virtual environment:</p>
    <ul>
      <li>On Windows (using Git Bash):
        <pre><code>source venv/Scripts/activate</code></pre>
      </li>
      <li>On macOS and Linux:
        <pre><code>source venv/bin/activate</code></pre>
      </li>
    </ul>
  </li>

  <li>
    <p>Your prompt should change to indicate that the virtual environment is active.</p>
  </li>

  <li>
    <p>Install the project dependencies (if any):</p>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li>
    <p>When you're done working on the project, you can deactivate the virtual environment:</p>
    <pre><code>deactivate</code></pre>
  </li>
</ol>

<p>Remember to activate the virtual environment each time you work on the project.</p>

<h2>Requirements</h2>
<ul>
<li><p>Python 3.9+</p>
</li></ul>
<pre><code>
</code></pre>
</code></pre>
