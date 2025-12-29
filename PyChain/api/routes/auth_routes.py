from flask import Blueprint, request, jsonify
import secrets
from eth_utils.crypto import keccak

auth_bp = Blueprint('auth', __name__)

nonces = {}

def pubkey_to_address(public_key):
    address_bytes = keccak(public_key.to_bytes())[12:]
    return f'Ox{address_bytes.hex()}'

@auth_bp.route('/challenge', methods=['POST'])
def challenge():
    data = request.get_json()
    address = data.get('address')
    if not address:
        return jsonify({'error': 'Missing address'}), 400
    nonce = secrets.token_hex(16)
    nonces[address] = nonce
    return jsonify({'challenge': nonce})

@auth_bp.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    address = data.get('address')
    signature_hex = data.get('signature')
    if not address or not signature_hex:
        return jsonify({'error': "Missing required parameters ADDRESS and/or SIGNATURE"})
    nonce = nonces.get(address)
    if not nonce:
        return jsonify({'error': f"No challenge found for address {address}"})
    verified = True # TODO: verify signature with eth_keys
    if not verified:
        return jsonify({'error': 'Invalid signature'})
    token = secrets.token_hex(16)
    return jsonify({'token': token})