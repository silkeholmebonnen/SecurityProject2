import random
from server import collect_shares_from_patients
from client import send_shares
from split_shares import split

patient_certfile = 'client3-cert.pem'
patient_keyfile = 'client3-key.pem'

shares = split("patient 3")

################        Acts as a client connecting to patient 1         ####################

send_shares(port=8080, name="patient 1", cert=patient_certfile, key=patient_keyfile, share=shares[0])

################        Acts as a client connecting to patient 2         ####################

send_shares(port=8081, name="patient 2", cert=patient_certfile, key=patient_keyfile, share=shares[1])

################        Acts as a server            ####################

component = collect_shares_from_patients(port=8082, cert=patient_certfile, key=patient_keyfile)
component += shares[2]

################        Acts as a client connecting to the hospital         ####################

send_shares(port=8090, name="hospital", cert=patient_certfile, key=patient_keyfile, share=component)