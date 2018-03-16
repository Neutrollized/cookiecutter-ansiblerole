title '{{ cookiecutter.repo_name | upper }}_ANSIBLE_ROLE'

control '{{ cookiecutter.repo_name }}-ansible-01' do
  impact 1.0
  title 'Validate Ansible configured {{ cookiecutter.repo_name | capitalize }} correctly'
  desc 'Ansible should configure {{ cookiecutter.repo_name | capitalize }} correctly.'

  describe package('somepackage') do
    it { should be_installed }
  end

  describe service('someservice') do
     it { should be_enabled }
     it { should be_running }
  end

  describe file('/some/file.txt') do
    it { should be_owned_by('root') }
    it { should be_grouped_into 'root' }
    its('mode') { should cmp '0700' }
  end

  describe file('/somefolder') do
    it { should be_directory }
    it { should be_owned_by('root') }
    it { should be_grouped_into 'root' }
    its('mode') { should cmp '0700' }
  end

 # More testing resources can be located at: http://inspec.io/docs/reference/resources/

end
