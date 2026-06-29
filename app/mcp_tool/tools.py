from connector import get_connection

def search_patients(patient_name):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
    
        query = """
        SELECT patient_id,patient_name,age,gender,diagnosis
        FROM patients
        WHERE patient_name ILIKE %s    
        """
        cursor.execute(
        query, (f"%{patient_name}%",)
        )

        result = cursor.fetchall()

        return result
    
    except Exception as e:

        print(f"Error:{e}")
        return None
    
    finally:
        if conn:
            conn.close()



def get_patient_history(patient_id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT patient_id,patient_name,age,gender,blood_group,
        diagnosis,
        admission_date,
        discharge_date,
        phone,
        city,
        emergency_contact
        FROM patients
        WHERE patient_id = %s    
        """

        cursor.execute(
        query,(patient_id,)
        )
        
        result = cursor.fetchone()
        return result
    
    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        if conn:
            conn.close()



def get_lab_results(patient_id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM lab_results
        WHERE patient_id = %s    
        """

        cursor.execute(
        query,(patient_id,)
        )

        result = cursor.fetchall()

        return result
    
    except Exception as e:
        print(f"Error:{e}")
        return None

    finally:
        if conn:
            conn.close()


def get_payment_summary(patient_id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT * 
        FROM billing
        WHERE patient_id=%s
        """
        cursor.execute(query,(patient_id,))

        result = cursor.fetchone()

        return result
    except Exception as e:
        print(f"Error:{e}")
        return None

    finally:
        if conn:
            conn.close()


