#----------------------------------------------------------------------------------------
#
# MIT License
#
# Copyright (c) 2023 maj0r, maj0rdesign
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#----------------------------------------------------------------------------------------

#
#
# Request signature creation/validation module
# Usage:
#   -- Change unSection to your unique value
#
#   print(Signature.create("user:maj0r", "pass:123", "type:create-module"))
#   print(Signature.validate("user:maj0r", "pass:123", "type:create-module", clientSignature="328b3e746dd4100274e48002a02818ac"))
#
#

import hashlib

global unSection
unSection = "<unique section>"

class Signature:
    def create_raw(rawString: str):
        return hashlib.md5(f"{unSection}{rawString}{unSection}".encode()).hexdigest()

    def create(*args: str):
        doneStr = f"{unSection}"
        for i in range(len(args)):
            if i != len(args):
                doneStr += args[i]
        doneStr += unSection

        return hashlib.md5(f"{unSection}{doneStr}{unSection}".encode()).hexdigest()

    def validate(*args: str, clientSignature: str):
        doneStr = f"{unSection}"
        for i in range(len(args)):
            if i != len(args):
                doneStr += args[i]
        doneStr += unSection

        return clientSignature == Signature.create_raw(doneStr)