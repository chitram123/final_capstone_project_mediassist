from fastmcp import FastMCP

from tools import(
    search_patients,
    get_patient_history,
    get_lab_results,
    get_payment_summary
)

## Initialize the MCP instance
mcp = FastMCP("Healthcare MCP",
              "Healthcare assistant for patient records, lab reports and billing information.")

## Register tools with the MCP instance
@mcp.tool()
def search_patient(patient_name: str):
    """
     Search patients by name.python app/mcp/server.py
    """
    
    return search_patients(patient_name)

@mcp.tool()
def patient_history(patient_id: int):
    """
    Get patient history.
    """
    return get_patient_history(patient_id)

@mcp.tool()
def lab_results(patient_id: int):
    """
    Get lab results of patient.
    """
    return get_lab_results(patient_id)

@mcp.tool()
def payment_summary(patient_id: int):
    """
    Get payment and billing information of patient.
    """
    return get_payment_summary(patient_id)

if __name__ == "__main__":
    print("********starting MCP server******")
    mcp.run()