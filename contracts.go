// Package contracts provide golang functions to read smart-contracts of snet-ecosystem
package contracts

import (
	"bytes"
	"embed"
)

type SnetContract string

const SingularityNetToken SnetContract = "SingularityNetToken"
const MultiPartyEscrow SnetContract = "MultiPartyEscrow"
const Registry SnetContract = "Registry"
const TokenStake SnetContract = "TokenStake"
const TokenConversionManager SnetContract = "TokenConversionManager"

var List = []SnetContract{SingularityNetToken, MultiPartyEscrow, Registry, TokenStake, TokenConversionManager}

//go:embed snet/contracts/resources/abi/*.json
var abifs embed.FS

//go:embed snet/contracts/resources/bytecode/*.json
var bytecodefs embed.FS

//go:embed snet/contracts/resources/networks/*.json
var networksfs embed.FS

func GetABI(name SnetContract) (content []byte) {
	content, _ = abifs.ReadFile("snet/contracts/resources/abi/" + string(name) + ".json")
	return content
}

// GetABIClean returns content without spaces and line breaks
func GetABIClean(name SnetContract) (content []byte) {
	return removeSpecialChars(GetABI(name))
}

func GetBytecode(name SnetContract) (content []byte) {
	content, _ = bytecodefs.ReadFile("snet/contracts/resources/bytecode/" + string(name) + ".json")
	return content
}

// GetBytecodeClean returns content without double quotes, spaces and line breaks
func GetBytecodeClean(name SnetContract) (content []byte) {
	result := bytes.ReplaceAll(GetBytecode(name), []byte(`"`), []byte(""))
	return removeSpecialChars(result)
}

// get addresses, events, and more for smart contracts for different networks
func GetNetworks(name SnetContract) (content []byte) {
	if name == TokenConversionManager {
		return
	}
	content, _ = networksfs.ReadFile("snet/contracts/resources/networks/" + string(name) + ".json")
	return content
}

// GetNetworksClean returns networks without spaces and line breaks
func GetNetworksClean(name SnetContract) (content []byte) {
	return removeSpecialChars(GetNetworks(name))
}

func removeSpecialChars(content []byte) []byte {
	result := bytes.ReplaceAll(content, []byte(` `), []byte(""))
	result = bytes.ReplaceAll(result, []byte(`\n`), []byte(""))
	result = bytes.ReplaceAll(result, []byte(`\r`), []byte(""))
	return bytes.ReplaceAll(result, []byte(`\t`), []byte(""))
}
