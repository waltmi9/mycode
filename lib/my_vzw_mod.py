#!/usr/bin/python3

ANSIBLE_METADATA = {
        'metadata_version': '1.1',
        'status': ['preview'],
        'supported_by': 'community'
}

RETURN = '''
original_message:
    desription: lorem ipsum
    type: str
message:
    description: ipsum lorum
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
            name=dict(type='str', required=True),
            new=dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        return result

    result['original_message'] = module.params['name']
    result['message'] = "Welcome to class, " + module.params['name']

    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'fail me':
        module.fail_json(msg="You requested the module to fail :(", **result)

    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()


