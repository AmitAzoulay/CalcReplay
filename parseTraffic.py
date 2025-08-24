class TsharkRunner:
    """
    Runs Tshark commands and parses output.
    """

    def run_tshark(pcap_path: str, display_filter: str, fields: List[str]) -> List[Dict[str, str]]:
        fields_str = " ".join(f"-e {field}" for field in fields)
        command = f"tshark -r \"{pcap_path}\" -Y \"{display_filter}\" -T fields {fields_str}"
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            lines = result.stdout.strip().split("\n")
            parsed_data = [dict(zip(fields, line.split("\t"))) for line in lines if line]
            return parsed_data
        except subprocess.CalledProcessError as e:
            print(f"Error running Tshark: {e}")
            return []

def main():

    runner = return TsharkRunner.run_tshark(
                self.pcap_path,
                "http",
                ["frame.number", "ip.src", "ip.dst"]
            )
    print(runner)

if __name__ == "__main__":
    main()