import subprocess
import argparse
import json

def inspect_image(image_name, stage):
    try:
        print(f"--- Analyzing Docker Image ({stage} stage): {image_name} ---")
        
        # Obtener metadata
        inspect_cmd = f"docker inspect {image_name}"
        metadata = json.loads(subprocess.check_output(inspect_cmd, shell=True))
        
        # Extraer detalles clave
        image_id = metadata[0]["Id"]
        size = metadata[0]["Size"]
        created = metadata[0]["Created"]
        env_vars = metadata[0]["Config"].get("Env", [])
        
        # Guardar reporte
        report = {
            "stage": stage,
            "image_id": image_id,
            "size": size,
            "created": created,
            "env_vars": env_vars,
        }
        with open(f"{stage}_image_report.json", "w") as f:
            json.dump(report, f, indent=4)

        print(f"Report saved: {stage}_image_report.json")
    except Exception as e:
        print(f"Error inspecting image: {e}")

def history_image(image_name, stage):
    try:
        print(f"--- Docker Image History ({stage} stage): {image_name} ---")
        history_cmd = f"docker history {image_name} --no-trunc --format '{{{{.CreatedBy}}}}'"
        result = subprocess.check_output(history_cmd, shell=True).decode("utf-8").strip()
        
        history_report = {"stage": stage, "history": result.split("\n")}
        with open(f"{stage}_image_history.json", "w") as f:
            json.dump(history_report, f, indent=4)

        print(f"History report saved: {stage}_image_history.json")
    except Exception as e:
        print(f"Error fetching history: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Docker Image")
    parser.add_argument("--image", required=True, help="Docker image name")
    parser.add_argument("--stage", required=True, help="Pipeline stage (import/build/push)")
    args = parser.parse_args()
    

    inspect_image(args.image, args.stage)

    history_image(args.image, args.stage)