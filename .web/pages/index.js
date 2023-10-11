import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Avatar, Box, Button, HStack, Image, Input, Link, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Table, TableContainer, Tbody, Td, Text, Th, Thead, Tr, useColorMode, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents.map((e) => ({...e})))
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {`http://localhost:8000`}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Box sx={{"width": "100%", "maxWidth": "960px", "bg": "white", "h": "100%", "px": [4, 12], "margin": "10px auto", "position": "relative"}}>
  <Link as={NextLink} href={`/`}>
  <Image src={`/logo.png`} sx={{"width": "auto", "height": "30px", "position": "absolute", "top": "0px", "left": "0px"}}/>
</Link>
  <Fragment>
  {isTrue(state.user_login) ? (
  <Fragment>
  <Link as={NextLink} href={`/profile`} sx={{"position": "absolute", "top": "0px", "right": "0px"}}>
  <Avatar size={`xs`}/>
</Link>
</Fragment>
) : (
  <Fragment>
  <Link as={NextLink} href={`/login`} sx={{"position": "absolute", "top": "0px", "right": "0px"}}>
  <Button size={`xs`}>
  {`Login / Sign up`}
</Button>
</Link>
</Fragment>
)}
</Fragment>
  <VStack>
  <HStack>
  <Input onChange={(_e0) => addEvents([Event("state.home_state.set_title", {value:_e0.target.value})], (_e0))} placeholder={`Look for a movie`} sx={{"max-width": "400px", "font-family": "Helvetica, sans-serif", "font-size": "12px"}} type={`text`}/>
  <Button isLoading={state.home_state.looking_database} onClick={(_e) => addEvents([Event("state.home_state.search_films_title", {})], (_e))} sx={{"max-width": "100px", "font-family": "Helvetica, sans-serif", "font-size": "8px"}}>
  {`Search`}
</Button>
</HStack>
  <Fragment>
  {isTrue(state.home_state.first_search) ? (
  <Fragment>
  <Text>
  {``}
</Text>
</Fragment>
) : (
  <Fragment>
  <TableContainer>
  <Table>
  <Thead sx={{"font-family": "Helvetica, sans-serif", "font-size": "12px"}}>
  <Tr>
  <Th>
  {`Title`}
</Th>
  <Th>
  {`Year`}
</Th>
  <Th>
  {`Genres`}
</Th>
  <Th>
  {`Runtime`}
</Th>
  <Th>
  {`Avg Rating`}
</Th>
  <Th>
  {`Num Votes`}
</Th>
</Tr>
</Thead>
  <Tbody sx={{"font-family": "Arial, sans-serif", "font-size": "8px"}}>
  {state.home_state.films_list.map((gdvzyhek, i) => (
  <Tr key={i}>
  <Td sx={{"maxWidth": "490px", "white-space": "normal", "padding": "1px"}}>
  <Link as={NextLink} href={state.home_state.films_link.at(i)}>
  {gdvzyhek.title}
</Link>
</Td>
  <Td sx={{"maxWidth": "80px", "white-space": "normal", "text-align": "center", "padding": "1px"}}>
  {gdvzyhek.year}
</Td>
  <Td sx={{"maxWidth": "150px", "white-space": "normal", "text-align": "center", "padding": "1px"}}>
  {gdvzyhek.genres}
</Td>
  <Td sx={{"maxWidth": "80px", "white-space": "normal", "text-align": "center", "padding": "1px"}}>
  {gdvzyhek.runtime}
</Td>
  <Td sx={{"maxWidth": "80px", "white-space": "normal", "text-align": "center", "padding": "1px"}}>
  {gdvzyhek.averageRating}
</Td>
  <Td sx={{"maxWidth": "80px", "white-space": "normal", "text-align": "center", "padding": "1px"}}>
  {gdvzyhek.numVotes}
</Td>
</Tr>
))}
</Tbody>
</Table>
</TableContainer>
</Fragment>
)}
</Fragment>
</VStack>
</Box>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
