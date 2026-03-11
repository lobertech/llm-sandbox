from llm_sandbox.session import SandboxSession

def test_simple_echo():
    print("Initializing SandboxSession for bash...")
    with SandboxSession(lang="bash", keep_template=False) as session:
        result = session.run('echo "hello from bash"')
        print(f"Result stdout: {result.stdout}")
        if result.stderr:
            print(f"Result stderr: {result.stderr}")

def test_bash_script():
    print("Testing bash script...")
    script = '''NAME="llm-sandbox"
if [ -n "$NAME" ]; then
    echo "Hello from $NAME"
fi'''
    with SandboxSession(lang="bash", keep_template=False) as session:
        result = session.run(script)
        print(f"Result stdout: {result.stdout}")
        if result.stderr:
            print(f"Result stderr: {result.stderr}")

def main():
    test_simple_echo()
    test_bash_script()

if __name__ == "__main__":
    main()
