# RandomPasswordPython
A library to create cryptographically secure passwords using the secrets library.

## How to use this library?

```python
import randPass
print(randPass.randPasswordsNumbers(40))
print(randPass.randPasswordLetters(40))
print(randPass.randPasswordsMedium(40))
print(randPass.randPasswordsHard(40))
```
Result:

```
python3 main.py

3698940820362566055716448857461075913724
tWOAGtCAuDLzGcQpHnUlaTHzjznwSZCMkfluRXFh
tZxUT4mu5wTVVJWPd5uqgyOtaHmXiMWFQbBO4XBX
[(Mj#BEF/8R.pfLSdeQy~<Dx"Vs%pdmE@97eIH$*
```
## randPasswordsNumbers
Generates only number passwords.

- How to generate them?

```python
length = 40
randPass.randPasswordsNumbers(length)
```

## randPasswordLetters
Only letter passwords are generated.

- How to generate them?

```python
length = 40
randPass.randPasswordLetters(length)
```

## randPasswordsMedium
A password is generated with digits and letters

- How to generate them?

```python
length = 40
randPass.randPasswordsMedium(length)
```

## randPasswordsHard
A password is generated with letters, numbers and special characters.

- How to generate them?

```python
length = 40
randPass.randPasswordsHard(length)
```