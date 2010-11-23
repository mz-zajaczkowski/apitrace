##########################################################################
#
# Copyright 2008-2009 VMware, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/

"""d3dcaps.h"""

from windows import *
from d3dtypes import *

D3DTRANSFORMCAPS = Flags(DWORD, [
    "D3DTRANSFORMCAPS_CLIP",
])

D3DTRANSFORMCAPS = Struct("D3DTRANSFORMCAPS", [
    (DWORD, "dwSize"),
    (DWORD, "dwCaps"),
])

D3DLIGHTINGCAPS = Struct("D3DLIGHTINGCAPS", [
    (DWORD, "dwSize"),
    (DWORD, "dwCaps"),
    (DWORD, "dwLightingModel"),
    (DWORD, "dwNumLights"),
])

D3DLIGHTINGMODEL = Flags(DWORD, [
    "D3DLIGHTINGMODEL_RGB",
    "D3DLIGHTINGMODEL_MONO",
])

D3DLIGHTCAPS = Flags(DWORD, [
    "D3DLIGHTCAPS_POINT",
    "D3DLIGHTCAPS_SPOT",
    "D3DLIGHTCAPS_DIRECTIONAL",
    "D3DLIGHTCAPS_PARALLELPOINT",
    "D3DLIGHTCAPS_GLSPOT",
])

D3DPRIMCAPS = Struct("D3DPRIMCAPS", [
    (DWORD, "dwSize"),
    (DWORD, "dwMiscCaps"),
    (DWORD, "dwRasterCaps"),
    (DWORD, "dwZCmpCaps"),
    (DWORD, "dwSrcBlendCaps"),
    (DWORD, "dwDestBlendCaps"),
    (DWORD, "dwAlphaCmpCaps"),
    (DWORD, "dwShadeCaps"),
    (DWORD, "dwTextureCaps"),
    (DWORD, "dwTextureFilterCaps"),
    (DWORD, "dwTextureBlendCaps"),
    (DWORD, "dwTextureAddressCaps"),
    (DWORD, "dwStippleWidth"),
    (DWORD, "dwStippleHeight"),
])

D3DPMISCCAPS = Flags(DWORD, [
    "D3DPMISCCAPS_MASKPLANES",
    "D3DPMISCCAPS_MASKZ",
    "D3DPMISCCAPS_LINEPATTERNREP",
    "D3DPMISCCAPS_CONFORMANT",
    "D3DPMISCCAPS_CULLNONE",
    "D3DPMISCCAPS_CULLCW",
    "D3DPMISCCAPS_CULLCCW",
])

D3DXD3DPRASTERCAPSXX = Flags(DWORD, [
    "D3DPRASTERCAPS_DITHER",
    "D3DPRASTERCAPS_ROP2",
    "D3DPRASTERCAPS_XOR",
    "D3DPRASTERCAPS_PAT",
    "D3DPRASTERCAPS_ZTEST",
    "D3DPRASTERCAPS_SUBPIXEL",
    "D3DPRASTERCAPS_SUBPIXELX",
    "D3DPRASTERCAPS_FOGVERTEX",
    "D3DPRASTERCAPS_FOGTABLE",
    "D3DPRASTERCAPS_STIPPLE",
    "D3DPRASTERCAPS_ANTIALIASSORTDEPENDENT",
    "D3DPRASTERCAPS_ANTIALIASSORTINDEPENDENT",
    "D3DPRASTERCAPS_ANTIALIASEDGES",
    "D3DPRASTERCAPS_MIPMAPLODBIAS",
    "D3DPRASTERCAPS_ZBIAS",
    "D3DPRASTERCAPS_ZBUFFERLESSHSR",
    "D3DPRASTERCAPS_FOGRANGE",
    "D3DPRASTERCAPS_ANISOTROPY",
    "D3DPRASTERCAPS_WBUFFER",
    "D3DPRASTERCAPS_TRANSLUCENTSORTINDEPENDENT",
    "D3DPRASTERCAPS_WFOG",
    "D3DPRASTERCAPS_ZFOG",
])

D3DPCMPCAPS = Flags(DWORD, [
    "D3DPCMPCAPS_NEVER",
    "D3DPCMPCAPS_LESS",
    "D3DPCMPCAPS_EQUAL",
    "D3DPCMPCAPS_LESSEQUAL",
    "D3DPCMPCAPS_GREATER",
    "D3DPCMPCAPS_NOTEQUAL",
    "D3DPCMPCAPS_GREATEREQUAL",
    "D3DPCMPCAPS_ALWAYS",
])

D3DPBLENDCAPS = Flags(DWORD, [
    "D3DPBLENDCAPS_ZERO",
    "D3DPBLENDCAPS_ONE",
    "D3DPBLENDCAPS_SRCCOLOR",
    "D3DPBLENDCAPS_INVSRCCOLOR",
    "D3DPBLENDCAPS_SRCALPHA",
    "D3DPBLENDCAPS_INVSRCALPHA",
    "D3DPBLENDCAPS_DESTALPHA",
    "D3DPBLENDCAPS_INVDESTALPHA",
    "D3DPBLENDCAPS_DESTCOLOR",
    "D3DPBLENDCAPS_INVDESTCOLOR",
    "D3DPBLENDCAPS_SRCALPHASAT",
    "D3DPBLENDCAPS_BOTHSRCALPHA",
    "D3DPBLENDCAPS_BOTHINVSRCALPHA",
])

D3DPSHADECAPS = Flags(DWORD, [
    "D3DPSHADECAPS_COLORFLATMONO",
    "D3DPSHADECAPS_COLORFLATRGB",
    "D3DPSHADECAPS_COLORGOURAUDMONO",
    "D3DPSHADECAPS_COLORGOURAUDRGB",
    "D3DPSHADECAPS_COLORPHONGMONO",
    "D3DPSHADECAPS_COLORPHONGRGB",
    "D3DPSHADECAPS_SPECULARFLATMONO",
    "D3DPSHADECAPS_SPECULARFLATRGB",
    "D3DPSHADECAPS_SPECULARGOURAUDMONO",
    "D3DPSHADECAPS_SPECULARGOURAUDRGB",
    "D3DPSHADECAPS_SPECULARPHONGMONO",
    "D3DPSHADECAPS_SPECULARPHONGRGB",
    "D3DPSHADECAPS_ALPHAFLATBLEND",
    "D3DPSHADECAPS_ALPHAFLATSTIPPLED",
    "D3DPSHADECAPS_ALPHAGOURAUDBLEND",
    "D3DPSHADECAPS_ALPHAGOURAUDSTIPPLED",
    "D3DPSHADECAPS_ALPHAPHONGBLEND",
    "D3DPSHADECAPS_ALPHAPHONGSTIPPLED",
    "D3DPSHADECAPS_FOGFLAT",
    "D3DPSHADECAPS_FOGGOURAUD",
    "D3DPSHADECAPS_FOGPHONG",
])

D3DPTEXTURECAPS = Flags(DWORD, [
    "D3DPTEXTURECAPS_PERSPECTIVE",
    "D3DPTEXTURECAPS_POW2",
    "D3DPTEXTURECAPS_ALPHA",
    "D3DPTEXTURECAPS_TRANSPARENCY",
    "D3DPTEXTURECAPS_BORDER",
    "D3DPTEXTURECAPS_SQUAREONLY",
    "D3DPTEXTURECAPS_TEXREPEATNOTSCALEDBYSIZE",
    "D3DPTEXTURECAPS_ALPHAPALETTE",
    "D3DPTEXTURECAPS_NONPOW2CONDITIONAL",
    "D3DPTEXTURECAPS_PROJECTED",
    "D3DPTEXTURECAPS_CUBEMAP",
    "D3DPTEXTURECAPS_COLORKEYBLEND",
])

D3DPTFILTERCAPS = Flags(DWORD, [
    "D3DPTFILTERCAPS_NEAREST",
    "D3DPTFILTERCAPS_LINEAR",
    "D3DPTFILTERCAPS_MIPNEAREST",
    "D3DPTFILTERCAPS_MIPLINEAR",
    "D3DPTFILTERCAPS_LINEARMIPNEAREST",
    "D3DPTFILTERCAPS_LINEARMIPLINEAR",
    "D3DPTFILTERCAPS_MINFPOINT",
    "D3DPTFILTERCAPS_MINFLINEAR",
    "D3DPTFILTERCAPS_MINFANISOTROPIC",
    "D3DPTFILTERCAPS_MIPFPOINT",
    "D3DPTFILTERCAPS_MIPFLINEAR",
    "D3DPTFILTERCAPS_MAGFPOINT",
    "D3DPTFILTERCAPS_MAGFLINEAR",
    "D3DPTFILTERCAPS_MAGFANISOTROPIC",
    "D3DPTFILTERCAPS_MAGFAFLATCUBIC",
    "D3DPTFILTERCAPS_MAGFGAUSSIANCUBIC",
])

D3DPTBLENDCAPS = Flags(DWORD, [
    "D3DPTBLENDCAPS_DECAL",
    "D3DPTBLENDCAPS_MODULATE",
    "D3DPTBLENDCAPS_DECALALPHA",
    "D3DPTBLENDCAPS_MODULATEALPHA",
    "D3DPTBLENDCAPS_DECALMASK",
    "D3DPTBLENDCAPS_MODULATEMASK",
    "D3DPTBLENDCAPS_COPY",
    "D3DPTBLENDCAPS_ADD",
])

D3DPTADDRESSCAPS = Flags(DWORD, [
    "D3DPTADDRESSCAPS_WRAP",
    "D3DPTADDRESSCAPS_MIRROR",
    "D3DPTADDRESSCAPS_CLAMP",
    "D3DPTADDRESSCAPS_BORDER",
    "D3DPTADDRESSCAPS_INDEPENDENTUV",
])

D3DSTENCILCAPS = Flags(DWORD, [
    "D3DSTENCILCAPS_KEEP",
    "D3DSTENCILCAPS_ZERO",
    "D3DSTENCILCAPS_REPLACE",
    "D3DSTENCILCAPS_INCRSAT",
    "D3DSTENCILCAPS_DECRSAT",
    "D3DSTENCILCAPS_INVERT",
    "D3DSTENCILCAPS_INCR",
    "D3DSTENCILCAPS_DECR",
])

D3DTEXOPCAPS = Flags(DWORD, [
    "D3DTEXOPCAPS_DISABLE",
    "D3DTEXOPCAPS_SELECTARG1",
    "D3DTEXOPCAPS_SELECTARG2",
    "D3DTEXOPCAPS_MODULATE",
    "D3DTEXOPCAPS_MODULATE2X",
    "D3DTEXOPCAPS_MODULATE4X",
    "D3DTEXOPCAPS_ADD",
    "D3DTEXOPCAPS_ADDSIGNED",
    "D3DTEXOPCAPS_ADDSIGNED2X",
    "D3DTEXOPCAPS_SUBTRACT",
    "D3DTEXOPCAPS_ADDSMOOTH",
    "D3DTEXOPCAPS_BLENDDIFFUSEALPHA",
    "D3DTEXOPCAPS_BLENDTEXTUREALPHA",
    "D3DTEXOPCAPS_BLENDFACTORALPHA",
    "D3DTEXOPCAPS_BLENDTEXTUREALPHAPM",
    "D3DTEXOPCAPS_BLENDCURRENTALPHA",
    "D3DTEXOPCAPS_PREMODULATE",
    "D3DTEXOPCAPS_MODULATEALPHA_ADDCOLOR",
    "D3DTEXOPCAPS_MODULATECOLOR_ADDALPHA",
    "D3DTEXOPCAPS_MODULATEINVALPHA_ADDCOLOR",
    "D3DTEXOPCAPS_MODULATEINVCOLOR_ADDALPHA",
    "D3DTEXOPCAPS_BUMPENVMAP",
    "D3DTEXOPCAPS_BUMPENVMAPLUMINANCE",
    "D3DTEXOPCAPS_DOTPRODUCT3",
])

D3DFVFCAPS = Flags(DWORD, [
    "D3DFVFCAPS_TEXCOORDCOUNTMASK",
    "D3DFVFCAPS_DONOTSTRIPELEMENTS",
])

D3DDD = Flags(DWORD, [
    "D3DDD_COLORMODEL",
    "D3DDD_DEVCAPS",
    "D3DDD_TRANSFORMCAPS",
    "D3DDD_LIGHTINGCAPS",
    "D3DDD_BCLIPPING",
    "D3DDD_LINECAPS",
    "D3DDD_TRICAPS",
    "D3DDD_DEVICERENDERBITDEPTH",
    "D3DDD_DEVICEZBUFFERBITDEPTH",
    "D3DDD_MAXBUFFERSIZE",
    "D3DDD_MAXVERTEXCOUNT",
])

D3DDEVCAPS = Flags(DWORD, [
    "D3DDEVCAPS_FLOATTLVERTEX",
    "D3DDEVCAPS_SORTINCREASINGZ",
    "D3DDEVCAPS_SORTDECREASINGZ",
    "D3DDEVCAPS_SORTEXACT",
    "D3DDEVCAPS_EXECUTESYSTEMMEMORY",
    "D3DDEVCAPS_EXECUTEVIDEOMEMORY",
    "D3DDEVCAPS_TLVERTEXSYSTEMMEMORY",
    "D3DDEVCAPS_TLVERTEXVIDEOMEMORY",
    "D3DDEVCAPS_TEXTURESYSTEMMEMORY",
    "D3DDEVCAPS_TEXTUREVIDEOMEMORY",
    "D3DDEVCAPS_DRAWPRIMTLVERTEX",
    "D3DDEVCAPS_CANRENDERAFTERFLIP",
    "D3DDEVCAPS_TEXTURENONLOCALVIDMEM",
    "D3DDEVCAPS_DRAWPRIMITIVES2",
    "D3DDEVCAPS_SEPARATETEXTUREMEMORIES",
    "D3DDEVCAPS_DRAWPRIMITIVES2EX",
    "D3DDEVCAPS_HWTRANSFORMANDLIGHT",
    "D3DDEVCAPS_CANBLTSYSTONONLOCAL",
    "D3DDEVCAPS_HWRASTERIZATION",
])

D3DVTXPCAPS = Flags(DWORD, [
    "D3DVTXPCAPS_TEXGEN",
    "D3DVTXPCAPS_MATERIALSOURCE7",
    "D3DVTXPCAPS_VERTEXFOG",
    "D3DVTXPCAPS_DIRECTIONALLIGHTS",
    "D3DVTXPCAPS_POSITIONALLIGHTS",
    "D3DVTXPCAPS_LOCALVIEWER",
])

D3DFDS = Flags(DWORD, [
    "D3DFDS_COLORMODEL",
    "D3DFDS_GUID",
    "D3DFDS_HARDWARE",
    "D3DFDS_TRIANGLES",
    "D3DFDS_LINES",
    "D3DFDS_MISCCAPS",
    "D3DFDS_RASTERCAPS",
    "D3DFDS_ZCMPCAPS",
    "D3DFDS_ALPHACMPCAPS",
    "D3DFDS_SRCBLENDCAPS",
    "D3DFDS_DSTBLENDCAPS",
    "D3DFDS_SHADECAPS",
    "D3DFDS_TEXTURECAPS",
    "D3DFDS_TEXTUREFILTERCAPS",
    "D3DFDS_TEXTUREBLENDCAPS",
    "D3DFDS_TEXTUREADDRESSCAPS",
])

D3DFINDDEVICESEARCH = Struct("D3DFINDDEVICESEARCH", [
    (DWORD, "dwSize"),
    (DWORD, "dwFlags"),
    (BOOL, "bHardware"),
    (D3DCOLORMODEL, "dcmColorModel"),
    (GUID, "guid"),
    (DWORD, "dwCaps"),
    (D3DPRIMCAPS, "dpcPrimCaps"),
])
LPD3DFINDDEVICESEARCH = Pointer(D3DFINDDEVICESEARCH)

D3DEXECUTEBUFFERDESC = Struct("D3DEXECUTEBUFFERDESC", [
    (DWORD, "dwSize"),
    (DWORD, "dwFlags"),
    (DWORD, "dwCaps"),
    (DWORD, "dwBufferSize"),
    (LPVOID, "lpData"),
])
LPD3DEXECUTEBUFFERDESC = Pointer(D3DEXECUTEBUFFERDESC)

D3DDEB = Flags(DWORD, [
    "D3DDEB_BUFSIZE",
    "D3DDEB_CAPS",
    "D3DDEB_LPDATA",
])

D3DDEBCAPS = Flags(DWORD, [
    "D3DDEBCAPS_SYSTEMMEMORY",
    "D3DDEBCAPS_VIDEOMEMORY",
    "D3DDEBCAPS_MEM",
])

D3DDEVINFO_TEXTUREMANAGER = Struct("D3DDEVINFO_TEXTUREMANAGER", [
    (BOOL, "bThrashing"),
    (DWORD, "dwApproxBytesDownloaded"),
    (DWORD, "dwNumEvicts"),
    (DWORD, "dwNumVidCreates"),
    (DWORD, "dwNumTexturesUsed"),
    (DWORD, "dwNumUsedTexInVid"),
    (DWORD, "dwWorkingSet"),
    (DWORD, "dwWorkingSetBytes"),
    (DWORD, "dwTotalManaged"),
    (DWORD, "dwTotalBytes"),
    (DWORD, "dwLastPri"),
])

D3DDEVINFO_TEXTURING = Struct("D3DDEVINFO_TEXTURING", [
    (DWORD, "dwNumLoads"),
    (DWORD, "dwApproxBytesLoaded"),
    (DWORD, "dwNumPreLoads"),
    (DWORD, "dwNumSet"),
    (DWORD, "dwNumCreates"),
    (DWORD, "dwNumDestroys"),
    (DWORD, "dwNumSetPriorities"),
    (DWORD, "dwNumSetLODs"),
    (DWORD, "dwNumLocks"),
    (DWORD, "dwNumGetDCs"),
])

D3DDEVICEDESC = Struct("D3DDEVICEDESC", [
    (DWORD, "dwSize"),
    (DWORD, "dwFlags"),
    (D3DCOLORMODEL, "dcmColorModel"),
    (DWORD, "dwDevCaps"),
    (D3DTRANSFORMCAPS, "dtcTransformCaps"),
    (BOOL, "bClipping"),
    (D3DLIGHTINGCAPS, "dlcLightingCaps"),
    (D3DPRIMCAPS, "dpcLineCaps"),
    (D3DPRIMCAPS, "dpcTriCaps"),
    (DWORD, "dwDeviceRenderBitDepth"),
    (DWORD, "dwDeviceZBufferBitDepth"),
    (DWORD, "dwMaxBufferSize"),
    (DWORD, "dwMaxVertexCount"),
    (DWORD, "dwMinTextureWidth"),
    (DWORD, "dwMinTextureHeight"),
    (DWORD, "dwMaxTextureWidth"),
    (DWORD, "dwMaxTextureHeight"),
    (DWORD, "dwMinStippleWidth"),
    (DWORD, "dwMaxStippleWidth"),
    (DWORD, "dwMinStippleHeight"),
    (DWORD, "dwMaxStippleHeight"),
    (DWORD, "dwMaxTextureRepeat"),
    (DWORD, "dwMaxTextureAspectRatio"),
    (DWORD, "dwMaxAnisotropy"),
    (D3DVALUE, "dvGuardBandLeft"),
    (D3DVALUE, "dvGuardBandTop"),
    (D3DVALUE, "dvGuardBandRight"),
    (D3DVALUE, "dvGuardBandBottom"),
    (D3DVALUE, "dvExtentsAdjust"),
    (DWORD, "dwStencilCaps"),
    (DWORD, "dwFVFCaps"),
    (DWORD, "dwTextureOpCaps"),
    (WORD, "wMaxTextureBlendStages"),
    (WORD, "wMaxSimultaneousTextures"),
])
LPD3DDEVICEDESC = Pointer(D3DDEVICEDESC)

D3DDEVICEDESC7 = Struct("D3DDEVICEDESC7", [
    (DWORD, "dwDevCaps"),
    (D3DPRIMCAPS, "dpcLineCaps"),
    (D3DPRIMCAPS, "dpcTriCaps"),
    (DWORD, "dwDeviceRenderBitDepth"),
    (DWORD, "dwDeviceZBufferBitDepth"),
    (DWORD, "dwMinTextureWidth"),
    (DWORD, "dwMinTextureHeight"),
    (DWORD, "dwMaxTextureWidth"),
    (DWORD, "dwMaxTextureHeight"),
    (DWORD, "dwMaxTextureRepeat"),
    (DWORD, "dwMaxTextureAspectRatio"),
    (DWORD, "dwMaxAnisotropy"),
    (D3DVALUE, "dvGuardBandLeft"),
    (D3DVALUE, "dvGuardBandTop"),
    (D3DVALUE, "dvGuardBandRight"),
    (D3DVALUE, "dvGuardBandBottom"),
    (D3DVALUE, "dvExtentsAdjust"),
    (DWORD, "dwStencilCaps"),
    (DWORD, "dwFVFCaps"),
    (DWORD, "dwTextureOpCaps"),
    (WORD, "wMaxTextureBlendStages"),
    (WORD, "wMaxSimultaneousTextures"),
    (DWORD, "dwMaxActiveLights"),
    (D3DVALUE, "dvMaxVertexW"),
    (GUID, "deviceGUID"),
    (WORD, "wMaxUserClipPlanes"),
    (WORD, "wMaxVertexBlendMatrices"),
    (DWORD, "dwVertexProcessingCaps"),
    (DWORD, "dwReserved1"),
    (DWORD, "dwReserved2"),
    (DWORD, "dwReserved3"),
    (DWORD, "dwReserved4"),
])
LPD3DDEVICEDESC7 = Pointer(D3DDEVICEDESC7)

D3DFINDDEVICERESULT = Struct("D3DFINDDEVICERESULT", [
    (DWORD, "dwSize"),
    (GUID, "guid"),
    (D3DDEVICEDESC, "ddHwDesc"),
    (D3DDEVICEDESC, "ddSwDesc"),
])
LPD3DFINDDEVICERESULT = Pointer(D3DFINDDEVICERESULT)

LPD3DENUMDEVICESCALLBACK = StdFunction(HRESULT, "LPD3DENUMDEVICESCALLBACK", [(Pointer(GUID), "lpGuid"), (LPSTR, "lpDeviceDescription"), (LPSTR, "lpDeviceName"), LPD3DDEVICEDESC, LPD3DDEVICEDESC, LPVOID])
LPD3DENUMDEVICESCALLBACK7 = StdFunction(HRESULT, "LPD3DENUMDEVICESCALLBACK7", [(LPSTR, "lpDeviceDescription"), (LPSTR, "lpDeviceName"), LPD3DDEVICEDESC7, LPVOID])

