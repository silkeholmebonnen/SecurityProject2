from server import collect_shares_from_patients
from client import send_shares
from split_shares import split

patient_certfile = 'client1-cert.pem'
patient_keyfile = 'client1-key.pem'

shares = split("patient 1")

################        Acts as a server            ####################

component = collect_shares_from_patients(port=8080, cert=patient_certfile, key=patient_keyfile)
component += shares[0]

################        Acts as a client connecting to patient 2         ####################

send_shares(port=8081, name="patient 2", cert=patient_certfile, key=patient_keyfile, share=shares[1])

################        Acts as a client connecting to patient 3         ####################

send_shares(port=8082, name="patient 3", cert=patient_certfile, key=patient_keyfile, share=shares[2])

################        Acts as a client connecting to the hospital         ####################

send_shares(port=8090, name="hospital", cert=patient_certfile, key=patient_keyfile, share=component)