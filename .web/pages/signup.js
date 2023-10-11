import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Image, Input, Link, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text, useColorMode } from "@chakra-ui/react"
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
  <Box sx={{"margin": "auto", "bg": "white", "border": "1px solid #eaeaea", "p": 4, "maxWidth": "400px", "borderRadius": "lg", "display": "flex", "flexDirection": "column", "alignItems": "center", "justifyContent": "center"}}>
  <Input onBlur={(_e0) => addEvents([Event("state.auth_state.set_username", {value:_e0.target.value})], (_e0))} placeholder={`Username`} sx={{"mb": 4}} type={`text`}/>
  <Input onBlur={(_e0) => addEvents([Event("state.auth_state.set_password", {value:_e0.target.value})], (_e0))} placeholder={`Password`} sx={{"mb": 4}} type={`password`}/>
  <Input onBlur={(_e0) => addEvents([Event("state.auth_state.set_confirm_password", {value:_e0.target.value})], (_e0))} placeholder={`Confirm password`} sx={{"mb": 4}} type={`password`}/>
  <Input onBlur={(_e0) => addEvents([Event("state.auth_state.set_email", {value:_e0.target.value})], (_e0))} placeholder={`Email`} sx={{"mb": 4}} type={`text`}/>
  <Button onClick={(_e) => addEvents([Event("state.auth_state.signup", {})], (_e))} sx={{"bg": "blue.500", "color": "white", "_hover": {"bg": "blue.600"}, "mb": 4}}>
  {`Sign up`}
</Button>
</Box>
  <Text sx={{"text-align": "center", "color": "gray.600"}}>
  {`Already have an account?  `}
  <Link as={NextLink} href={`/login`} sx={{"color": "blue.500"}}>
  {`Sign in here.`}
</Link>
</Text>
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
